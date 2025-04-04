import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('localhost',9001))

cmd = 'GET http://localhost/romeo.txt HTTP1.0\r\n\r\n'.encode('utf-8')
client_socket.send(cmd)

while True:
    data = client_socket.recv(9000)
    if len(data) < 1:
        break
    print(data.decode('utf-8'))
    break
client_socket.close()

