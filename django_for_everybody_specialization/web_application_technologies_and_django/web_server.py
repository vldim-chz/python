import socket
import  re
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost', 9001))
server_socket.listen()

try:

    while True:
        (client_socket, address) = server_socket.accept()
        data = client_socket.recv(1024).decode('utf-8')
        pattern = '^GET http://localhost/([A-za-z0-9]+\.txt)'
        print(data)
        match = re.search(pattern, data)
        if match:
            name = match.group(1)
            with open(name, 'r') as file:
                client_socket.send(file.read().encode('utf-8'))
        else:
            print(match)
            break




except KeyboardInterrupt:
    print('Shutting down')
except Exception as e:
    print("Unexpected error:")
    print(e)
