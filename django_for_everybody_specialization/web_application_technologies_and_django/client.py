import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('data.pr4e.org', 80))

# alternative to encode(utf-8)
# cmd = b'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'
# In case you want to add some headers then you should do something like this
# 'GET /path/to/resource HTTP/1.1\r\nHost: www.example.com\r\nUser-Agent: PythonSocketClient/1.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nConnection: close\r\n\r\n'
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode('utf-8')
client_socket.send(cmd)

while True:
    data = client_socket.recv(1024)
    if len(data)<1:
        break
    print(data.decode('utf-8'))
client_socket.close()
