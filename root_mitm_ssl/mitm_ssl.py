import re
from mitmproxy.http import HTTPResponse

FORCE_HTTPS = False
FILTER_CONTENT = ['text/plain', 'text/html', 'text/css']
OK_REDIRECT = ['t.co']

known_secure_hosts = set()


def http_connect(flow):
    flow.response = HTTPResponse.make(418)


def popHeader(hdr, toPop):
    keys = [e for e in hdr if e.lower() == toPop.lower()]
    for k in keys:
        hdr.pop(k, None)


def request(flow):
    popHeader(flow.request.headers, 'Proxy-Connection')
    host = flow.request.pretty_host
    if host.endswith('.ssl'):
        flow.request.scheme = 'https'
        flow.request.port = 443
        origHost = host.replace('.ssl', '')
        known_secure_hosts.add(origHost)
        flow.request.host = origHost
    if flow.request.scheme != 'https' and FORCE_HTTPS:
        newUrl = createSslUrl(flow.request.url)
        flow.response = HTTPResponse.make(301, '', {'Location': newUrl})
        return
    # TODO: we may have the .ssl suffix in them; would be nice just to replace
    popHeader(flow.request.headers, 'Referer')
    popHeader(flow.request.headers, 'Origin')
    flow.request.url = flow.request.url.replace('.ssl/', '/')
    print('request(' + flow.request.url + ')', flow.request.headers)


def createSslUrl(orig):
    us = orig.replace('https://', 'http://')
    ul = us.split('/')
    if not ul[2].endswith('.ssl'):
        ul[2] = ul[2] + '.ssl'
    return '/'.join(ul)


def chgRegexp(data, regexp, target=b''):
    return re.sub(regexp, target, data, flags=re.IGNORECASE)


def response(flow):
    rHeaders = flow.response.headers
    if rHeaders.get('Location', '').startswith('https://'):
        newUrl = createSslUrl(rHeaders.get('Location', ''))
        flow.response = HTTPResponse.make(301, newUrl, {'Location': newUrl})
        return

    rCnt = flow.response.content
    if len(FILTER_CONTENT) > 0:
        ct = rHeaders.get('Content-Type', 'none')
        rlk = [k for k in rHeaders.keys() if k.lower() == 'content-length']
        print('FILTER_CONTENT;', ct)
        isAccepted = len(rCnt) == 0
        if len(rlk) > 0:
            isAccepted = isAccepted or int(rHeaders[rlk[0]]) == 0
        for f in FILTER_CONTENT:
            isAccepted = isAccepted or ct.startswith(f)
        if not isAccepted:
            flow.response = HTTPResponse.make(404)
            return

    for ksh in known_secure_hosts:
        bksh = ksh.encode()
        if bksh in rCnt:
            rCnt = rCnt.replace(bksh, bksh + b'.ssl')
    popHeader(rHeaders, 'Content-Security-Policy')
    popHeader(rHeaders, 'Strict-Transport-Security')
    popHeader(rHeaders, 'Public-Key-Pins')
    rCnt = chgRegexp(rCnt, b'([^q].)https://', b'\\1http://')
    rCnt = chgRegexp(rCnt, b'integrity="sha256-[A-Za-z0-9+/=]*"')
    rCnt = chgRegexp(rCnt, b'crossorigin=["\']anonymous["\']')
    rCnt = chgRegexp(
        rCnt, b'<meta[^<>]*http-equiv=["\']Content-Security-Policy[^<>]*>')

    cookies = rHeaders.get_all('Set-Cookie')
    cookies = [re.sub(r';\s*[Ss]ecure\s*', '', s) for s in cookies]
    rHeaders.set_all('Set-Cookie', cookies)

    if flow.request.host not in OK_REDIRECT:
        rCnt = chgRegexp(rCnt, b'<meta[^<>]*http-equiv=["\']refresh[^<>]*>')

    flow.response.content = rCnt
    print('response(' + flow.request.url + ')', flow.response.headers)
