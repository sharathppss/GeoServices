import argparse
from http.server import HTTPServer
from GeoServiceHandler import GeoServiceHandler


def start_server(ip, port):
    """

    :param ip: ipaddress for the server to start at
    :param port: port where to start
    exception raised on failure to start server
    """
    httpd = HTTPServer((ip, port), GeoServiceHandler)
    print('GeoServer running at {}:{}'.format(ip, port))
    httpd.serve_forever()


if __name__ == '__main__':

    argparser = argparse.ArgumentParser()
    argparser.add_argument('--ipadd', type=str, default='127.0.0.1', help='Host server ip address')
    argparser.add_argument('--port', type=int, default=4444, help='Host server port number')
    args, _ = argparser.parse_known_args()

    start_server(args.ipadd, args.port)
