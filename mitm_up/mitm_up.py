from mitmproxy.http import HTTPResponse
from collections import defaultdict
import time

ignoreHosts = ['192.168.']
insecure_urls = defaultdict(float)


def request(flow):
    url = flow.request.pretty_url
    host = flow.request.pretty_host
    print('request():', host, url)
    if any(map(lambda s: host.startswith(s), ignoreHosts)):
        return
    resp = HTTPResponse.make(
        303, url, {
            'Content_Type': "text/html",
            'Location': url.replace('http://', 'https://', 1)
        })
    now = time.time()
    if insecure_urls[url] + 61 > now:
        resp = HTTPResponse.make(500, "mitm seen before" + url, {})
    if len(insecure_urls) > 5 * 1024:
        print('request(): insecure_urls.clear()')
        insecure_urls.clear()
    insecure_urls[url] = now
    flow.response = resp
