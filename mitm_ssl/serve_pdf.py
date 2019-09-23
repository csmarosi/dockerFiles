#!/usr/bin/env python3
import os
import requests
import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

proxies = {'http': 'http://127.0.0.1:8080'}
http_get_coverage = 0


class FileGetter(BaseHTTPRequestHandler):
    def do_GET(self):
        url = 'http://' + '/'.join(self.path.split('/')[1:])
        r = requests.get(url, proxies=proxies)
        self.send_response(r.status_code)
        for h in (
                'Content-Type',
                'Content-Length',
                'Last-Modified',
        ):
            if h in r.headers:
                self.send_header(h, r.headers[h])
        cl = 'Content-Length'
        if cl not in r.headers:
            self.send_header(cl, len(r.content))
        self.end_headers()
        self.wfile.write(r.content)
        global http_get_coverage
        http_get_coverage += 1


def main():
    PDF_PORT = int(os.environ.get('PDF_PORT', ''))
    server_address = ('', PDF_PORT)
    httpd = HTTPServer(server_address, FileGetter)
    t = threading.Thread(target=httpd.serve_forever, args=())
    t.start()
    while http_get_coverage < 1:
        time.sleep(.1)


if __name__ == '__main__':
    main()
