import re
from mitmproxy.http import HTTPResponse


def request(flow):
    host = flow.request.headers.get('Host', '')
    if host.endswith('.https'):
        flow.request.scheme = 'https'
        flow.request.port = 443
        origHost = host.replace('.https', '')
        flow.request.host = origHost
    elif host.endswith('.http'):
        flow.request.scheme = 'http'
        flow.request.port = 80
        origHost = host.replace('.http', '')
        flow.request.host = origHost
    else:
        flow.response = HTTPResponse.make(418)
    if False:
        print('requestH(' + flow.request.url + ')', flow.request.headers)


def rmRegexp(data, regexp):
    return re.sub(regexp, b'', data, flags=re.IGNORECASE)


def response(flow):
    rCnt = flow.response.content
    rCnt = rmRegexp(rCnt, b'<iframe[^<]*</iframe>')
    rCnt = rmRegexp(rCnt, b'<script[^<]*</script>')
    rCnt = rmRegexp(rCnt, b'<img[^>]*/>')
    flow.response.content = rCnt
