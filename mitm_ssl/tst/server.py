from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import ssl
import sys

PdfData = '''
%PDF-1.2
9 0 obj
<<
>>
stream
BT/ 9 Tf(Random BZON75HQ6NDR text in a PDF file)' ET
endstream
endobj
4 0 obj
<<
/Type /Page
/Parent 5 0 R
/Contents 9 0 R
>>
endobj
5 0 obj
<<
/Kids [4 0 R ]
/Count 1
/Type /Pages
/MediaBox [ 0 0 99 9 ]
>>
endobj
3 0 obj
<<
/Pages 5 0 R
/Type /Catalog
>>
endobj
trailer
<<
/Root 3 0 R
>>
%%EOF
'''

FormHtml = '''
<form action="/posted" method="post">
<textarea name="thetext" rows="20" cols="80">
some text
</textarea>
<input type="hidden" name="continue" value="https://testsite/somelink">
<input id="mybutton" type="submit" value="send">
</form>'''

LinkStr = '''
<a id="mylink" href="https://testsite/target">https://testsite/target</a>
'''

JsonStr = r'{"content":"href=\"https:\/\/twitter.com\/httpseverywhere\"\n\t"}'

httpPort = None


class MyServer(BaseHTTPRequestHandler):
    def writeKV(self, k, v):
        myStr = '<p>%s|%s</p>\n' % (k, v)
        self.wfile.write(myStr.encode())

    def redirect(self):
        self.send_response(302)
        self.send_header('Location', 'https://testsite:9832/redirected')
        self.send_header('Set-Cookie', 'test=magic; Secure; Domain=testsite')
        self.end_headers()

    def sendHtmlOk(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')

    def createLink(self):
        self.sendHtmlOk()
        self.end_headers()
        self.wfile.write(LinkStr.encode())

    def postForm(self):
        self.sendHtmlOk()
        self.end_headers()
        self.wfile.write(FormHtml.encode())

    def echoInfo(self):
        self.sendHtmlOk()
        self.end_headers()

        portStr = '<p>httpPort=' + str(httpPort) + '</p>\n'
        self.wfile.write(portStr.encode())
        self.writeKV('self.path', self.path)
        for h in self.headers:
            self.writeKV(h, self.headers[h])

    def ctPdf(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/pdf')
        self.end_headers()
        self.wfile.write(PdfData.encode())

    def json(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/json')
        self.end_headers()
        self.wfile.write(JsonStr.encode())

    def do_GET(self):
        if self.path == '/redirect':
            self.redirect()
            return
        elif self.path == '/link':
            self.createLink()
            return
        elif self.path == '/postform':
            self.postForm()
            return
        elif self.path.endswith('pdf'):
            self.ctPdf()
            return
        elif self.path == '/json':
            self.json()
            return
        self.echoInfo()

    def do_POST(self):
        self.echoInfo()
        length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(length).decode('utf-8')
        self.writeKV('post_data', post_data)


def main():
    global httpPort
    if len(sys.argv) > 1 and sys.argv[1] == "80":
        httpPort = 80
        myServer = HTTPServer(('0.0.0.0', httpPort), MyServer)
    else:
        httpPort = 443
        myServer = HTTPServer(('0.0.0.0', httpPort), MyServer)
        myServer.socket = ssl.wrap_socket(myServer.socket,
                                          server_side=True,
                                          certfile='/mitm_test/pemfile.pem')
    myServer.serve_forever()
    myServer.server_close()


if __name__ == '__main__':
    main()
