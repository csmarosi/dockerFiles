import os
import re
from mitmproxy.http import HTTPResponse

FILTER_CONTENT = None
FORCE_HTTPS = None
LOG_LEVEL = None
PDF_PORT = None


def start():
    global FILTER_CONTENT
    global FORCE_HTTPS
    global LOG_LEVEL
    global PDF_PORT
    FILTER_CONTENT = False if os.getenv('FILTER_CONTENT', '') == '0' else True
    FORCE_HTTPS = True if os.environ.get('FORCE_HTTPS', '') == '1' else False
    LOG_LEVEL = int(os.environ.get('LOG_LEVEL', '0'))
    pdf = os.environ.get('PDF_PORT', '')
    if len(pdf) > 0:
        PDF_PORT = pdf


javaScript = (
    'text/javascript',
    'application/javascript',
    'text/json',
    'application/json',
)
ALLOWED_CONTENT_TYPES = ('text/plain', 'text/html', 'text/css') + javaScript
OK_REDIRECT = (
    't.co',
    'accounts.google.com',
    'encrypted.google.com',
    'www.google.com',
)

TOR_UA = 'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0'

dnsRegExp = b'([0-9a-zA-Z.-]*)'


def http_connect(flow):
    flow.response = HTTPResponse.make(403)


def _createHttpsUrl(orig):
    return re.sub(r'http://([^/]*).ssl(.*)',
                  r'https://\1\2',
                  orig,
                  flags=re.IGNORECASE)


def _iKeys(myDict, key):
    return [e for e in myDict if e.lower() == key.lower()]


def _iGet(myDict, key, defaultValue='none'):
    ks = _iKeys(myDict, key)
    if len(ks) == 0:
        return defaultValue
    elif len(ks) == 1:
        return myDict[ks[0]]
    else:
        raise ValueError('header could be lower or upper case, but not both')


def _changeHeader(hdr, toChg, newData=None):
    for k in _iKeys(hdr, toChg):
        if '.ssl' == newData:
            hdr[k] = _createHttpsUrl(hdr[k])
        elif newData:
            hdr[k] = newData
        else:
            hdr.pop(k, None)


def _sanitizeLocation(orig):
    us = orig.replace('https://', 'http://', 1)
    # Specifying custom port is forbidden
    us = re.sub(':[0-9][0-9]*', '', us)
    ul = us.split('/')
    if orig.startswith('https'):
        ul[2] = ul[2] + '.ssl'
    return '/'.join(ul)


def request(flow):
    if LOG_LEVEL is None:
        start()
    _changeHeader(flow.request.headers, 'Proxy-Connection')
    _changeHeader(flow.request.headers, 'X-Requested-With')
    flow.remote_server = True
    flow.own_response = False
    if '127.0.0.1' in flow.request.pretty_host:
        urls = flow.request.url.split('/')
        flow.request.url = '/'.join(urls[:2] + urls[3:])
        flow.remote_server = False
    host = flow.request.pretty_host
    if host.endswith('.ssl'):
        flow.request.scheme = 'https'
        flow.request.port = 443
        flow.request.url = flow.request.url.replace('.ssl/', '/', 1)
    if flow.request.scheme != 'https' and FORCE_HTTPS:
        flow.request.scheme = 'https'
        newUrl = _sanitizeLocation(flow.request.url)
        flow.response = HTTPResponse.make(301, '', {'Location': newUrl})
        flow.own_response = True
        return
    if flow.remote_server and PDF_PORT and flow.request.url.endswith('.pdf'):
        parts = _sanitizeLocation(flow.request.url).split('/')
        flow.request.port = int(PDF_PORT)
        newUrl = '/'.join(parts[:2] + ['127.0.0.1:' + PDF_PORT] + parts[2:])
        flow.response = HTTPResponse.make(302, '', {'Location': newUrl})
        flow.own_response = True
        return
    _changeHeader(flow.request.headers, 'Referer', '.ssl')
    _changeHeader(flow.request.headers, 'Origin', '.ssl')
    _changeHeader(flow.request.headers, 'User-Agent', TOR_UA)
    _changeHeader(
        flow.request.headers, 'Accept',
        'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    _changeHeader(flow.request.headers, 'Accept-Language', 'en-US,en;q=0.5')
    uirh = 'Upgrade-Insecure-Requests'
    if not _iGet(flow.request.headers, uirh, None):
        flow.request.headers[uirh] = '1'
    newReqData = re.sub(b'http%3A%2F%2F' + dnsRegExp + b'.ssl',
                        b'https%3A%2F%2F' + b'\\1',
                        flow.request.content,
                        flags=re.IGNORECASE)
    # Touch content only if needed:
    if newReqData != flow.request.content:
        if LOG_LEVEL > 0:
            print('newReqData !=;', flow.request.url)
        flow.request.content = newReqData
    if LOG_LEVEL > 0:
        print('requestH(' + flow.request.url + ')', flow.request.headers)
    if LOG_LEVEL > 1:
        print('requestC(' + flow.request.url + ')', flow.request.content)


def _rmRegexp(data, regexp):
    return re.sub(regexp, b'', data, flags=re.IGNORECASE)


def response(flow):
    if LOG_LEVEL is None:
        start()
    if flow.own_response:
        return
    if LOG_LEVEL > 0:
        print('responseH(' + flow.request.url + ')', flow.response.headers)
    rHeaders = flow.response.headers

    ct = _iGet(rHeaders, 'content-type')
    if LOG_LEVEL > 1:
        doPrint = True
        for i in ('image'):
            if i in ct:
                doPrint = False
        if doPrint:
            print('responseC(' + flow.request.url + ')', flow.response.content)

    if _iGet(rHeaders, 'Location').startswith('http'):
        newUrl = _sanitizeLocation(_iGet(rHeaders, 'Location'))
        rHeaders[_iKeys(rHeaders, 'Location')[0]] = newUrl

    rCnt = flow.response.content
    if LOG_LEVEL > 0:
        print('FILTER_CONTENT;', ct)
    if FILTER_CONTENT:
        isAccepted = len(rCnt) == 0
        for f in ALLOWED_CONTENT_TYPES:
            isAccepted = isAccepted or ct.startswith(f)
        if not isAccepted and flow.remote_server:
            flow.response = HTTPResponse.make(404)
            return

    _changeHeader(rHeaders, 'Content-Security-Policy')
    _changeHeader(rHeaders, 'Strict-Transport-Security')
    _changeHeader(rHeaders, 'Public-Key-Pins')
    cookies_old = rHeaders.get_all('Set-Cookie')
    cookies_new = []
    for s in cookies_old:
        sn = re.sub(r';\s*[Ss]ecure\s*', '', s)
        cookies_new.append(sn)
        if 'domain=' in sn.lower():
            sn = re.sub('domain\s*=\s*' + dnsRegExp.decode('utf-8'),
                        'domain=' + r'\1.ssl',
                        sn,
                        flags=re.IGNORECASE)
            cookies_new.append(sn)
    rHeaders.set_all('Set-Cookie', cookies_new)
    if LOG_LEVEL > 1:
        print('responseH(' + flow.request.url + ') cookies', cookies_new)

    # Replace content only in text; https is filtered out anyway.
    doNotTouch = True
    for typ in (
            'text/html',
            'text/json',
    ):
        if typ in ct:
            doNotTouch = False
    if doNotTouch:
        return

    for urlPrefix in (
            b'"https://',
            b'" https://',
            b'url=https://',
            b'\(https://',
            b"'https://",
            b'href=\\\\"https:\\\\/\\\\/',
    ):
        rCnt = re.sub(urlPrefix + dnsRegExp,
                      urlPrefix.replace(b's:', b':') + b'\\1.ssl',
                      rCnt,
                      flags=re.IGNORECASE)
    rCnt = _rmRegexp(
        rCnt, b'<meta[^<>]*http-equiv=["\']Content-Security-Policy[^<>]*>')
    if flow.request.host not in OK_REDIRECT:
        rCnt = _rmRegexp(rCnt, b'<meta[^<>]*http-equiv=["\']refresh[^<>]*>')
        rCnt = _rmRegexp(rCnt, b'class="NoScriptForm[^"]*"')  # twitter

    flow.response.content = rCnt
