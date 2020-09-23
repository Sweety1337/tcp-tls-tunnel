from http.client import HTTPConnection
import sys
from urllib.parse import urlparse
import urllib3


sys.path.append('../')

from agent import TunnelHttpAgent


url = 'https://www.ja3er.com/json'
timeout = 5
port = 443
headers = urllib3.make_headers(
    keep_alive=True,
    disable_cache=True,
    accept_encoding=True,
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
)


def ja3er():
    parsed_url = urlparse(url)
    host = parsed_url.netloc
    tunnelHttpAgent = TunnelHttpAgent(
        host='IP',
        port=443,
        server_name=host,
        server_port=port,
        auth={
            'login': 'test-login',
            'password': 'test-password'
        },
        timeout=timeout,
        proxy=None,
        client=None,
    )
    connection = HTTPConnection(host=host, port=port, timeout=timeout)
    connection.sock = tunnelHttpAgent.sock
    connection.request(method='GET', url=parsed_url.path, body=parsed_url.query, headers=headers)
    response = connection.getresponse().read().decode('utf-8')
    connection.close()
    tunnelHttpAgent.close()

    print(response)


if __name__ == '__main__':
    ja3er()
