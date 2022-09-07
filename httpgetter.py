import socket

def http_get(url):
    result = ''
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            result = result + str(data, 'utf8')
        else:
            break
    s.close()
    return result

def get_body(response):
    return response[response.find('\r\n\r\n')+4:]
