from mitmproxy.models import HTTPResponse
from netlib.http import Headers
from collections import defaultdict
import time
from mitmproxy import ctx as context

ignoreHosts = ['192.168.']


def start():
    context.insecure_urls = defaultdict(float)


def request(flow):
    url = flow.request.pretty_url
    host = flow.request.pretty_host
    print('request():', host, url)
    if any(map(lambda s: host.startswith(s), ignoreHosts)):
        return
    resp = HTTPResponse(
        "HTTP/1.1",
        303,
        "See Other",
        Headers(
            Content_Type="text/html",
            Location=url.replace('http://', 'https://', 1)),
        url)
    now = time.time()
    if context.insecure_urls[url] + 61 > now:
        resp = HTTPResponse(
            "HTTP/1.1",
            500,
            "mitm seen before",
            Headers(Content_Type="text/html"),
            url)
    if len(context.insecure_urls) > 5 * 1024:
        print('request(): insecure_urls.clear()')
        context.insecure_urls.clear()
    context.insecure_urls[url] = now
    flow.response = resp
