from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import os
import time

COVERAGE_CMD = ' coverage run -p --branch --source . '


class MyServer(BaseHTTPRequestHandler):
    def json(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/json')
        self.end_headers()
        self.wfile.write(b'{"result": "OK"}')

    def get_dockercmd(self, path):
        for fn in ('entrypoint.sh', 'Dockerfile', 'Dockerfile.sh'):
            file_full_path = path + fn
            if not os.path.isfile(file_full_path):
                continue
            with open(file_full_path, 'r') as f:
                lines = f.read().split('\n')
                eline = [i for i in lines if 'ENTRYPOINT' in i]
            if len(eline) > 0:
                dockercmd = eline[0].split('"')[1::2]
            else:
                dockercmd = lines[-2].strip().split(' ')
            return dockercmd

    def coverage_cmd(self, path):
        os.system('pkill -f bin/coverage')
        time.sleep(1)
        os.system('rm -rf htmlcov/ .coverage* __pycache__/')
        dockercmd = self.get_dockercmd(path)
        mitmcmd = '/usr/local/bin/' + ' '.join(dockercmd) + ' --ssl-insecure &'
        mitmcmd = mitmcmd.replace('/mitm/', path)
        covercmd = COVERAGE_CMD + mitmcmd
        print(covercmd)
        return covercmd

    # TODO: add
    # --no-anticache
    # --no-anticomp
    # --no-http2
    def coverage_start_ssl(self):
        covercmd = self.coverage_cmd('/dockerFiles/mitm_ssl/')
        os.system('LOG_LEVEL=5 FILTER_CONTENT=0' + covercmd)
        os.system('LOG_LEVEL=5 FILTER_CONTENT=0 FORCE_HTTPS=1' +
                  covercmd.replace('8080', '8081'))
        os.system('LOG_LEVEL=5' + covercmd.replace('8080', '8082'))
        os.system('LOG_LEVEL=5 PDF_PORT=1234' +
                  covercmd.replace('8080', '8083'))
        os.system('PDF_PORT=1234' + COVERAGE_CMD +
                  '/dockerFiles/mitm_ssl/serve_pdf.py &')

    def coverage_start(self):
        covercmd = self.coverage_cmd(os.getcwd() + '/')
        os.system(covercmd)
        trans = '--mode transparent --quiet'
        if trans in covercmd:
            os.system(covercmd.replace('8080', '8081').replace(trans, ''))

    def coverage_collect(self):
        os.system('pkill -f bin/coverage')
        os.system('coverage combine && coverage report && coverage html')
        os.system('rm -rf .coverage* __pycache__/')

    def do_GET(self):
        os.chdir('/dockerFiles/mitm_ssl')
        if self.path == '/coverage_start':
            self.coverage_start_ssl()
            self.json()
            return
        elif self.path == '/coverage_start_up':
            os.chdir('/dockerFiles/mitm_up')
            self.coverage_start()
            self.json()
            return
        elif self.path == '/coverage_start_http':
            os.chdir('/dockerFiles/mitm_http')
            self.coverage_start()
            self.json()
        elif self.path == '/coverage_collect':
            self.coverage_collect()
            self.json()
            return
        elif self.path == '/coverage_collect_up':
            os.chdir('/dockerFiles/mitm_up')
            self.coverage_collect()
            self.json()
            return
            return
        elif self.path == '/coverage_collect_http':
            os.chdir('/dockerFiles/mitm_http')
            self.coverage_collect()
            self.json()
            return


def main():
    myServer = HTTPServer(('0.0.0.0', 4280), MyServer)
    myServer.serve_forever()
    myServer.server_close()


if __name__ == '__main__':
    main()
