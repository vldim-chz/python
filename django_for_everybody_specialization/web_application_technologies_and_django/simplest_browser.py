import socket

from pycparser.c_ast import While

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('data.pr4e.org', 80))

# alternative to encode(utf-8)
# cmd = b'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode('utf-8')
client_socket.send(cmd)

while True:
    data = client_socket.recv(1024)
    if len(data)<1:
        break
    print(data.decode('utf-8'))
client_socket.close()
