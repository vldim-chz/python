# 1. Import necessary components from the socket module
from socket import *

# 2. Define the main server function
def create_server():
    # 3. Create a server socket object
    #    AF_INET: Use IPv4 addresses.
    #    SOCK_STREAM: Use TCP (a reliable, connection-oriented protocol).
    server_socket = socket(AF_INET, SOCK_STREAM)

    # 4. Start a try block for error handling
    try :
        # 5. Bind the socket to a specific address and port
        #    'localhost': Listen only on the local machine (127.0.0.1).
        #    9000: The port number the server will listen on.
        server_socket.bind(('localhost',9000))

        # 6. Enable the server to accept connections
        #    5: The backlog - maximum number of queued connections before refusing new ones.
        server_socket.listen(5)

        # 7. Start an infinite loop to continuously handle client connections
        while True:
            # 8. Wait for and accept a new client connection
            #    This is a *blocking* call - execution pauses here until a client connects.
            #    client_socket: A *new* socket object for communication with this specific client.
            #    address: A tuple containing the client's IP address and port.
            (client_socket, address) = server_socket.accept()

            # 9. Receive data (HTTP request) from the client
            #    recv(5000): Read up to 5000 bytes from the client socket.
            #    .decode(): Convert the received bytes into a string (assuming UTF-8).
            rd = client_socket.recv(5000).decode()

            # 10. Basic parsing of the request (split into lines)
            pieces = rd.split("\n")
            # 11. Print the first line of the request (e.g., "GET / HTTP/1.1") if it exists
            if len(pieces) > 0: print(pieces[0])

            # 12. Construct the HTTP response as a string
            #     - Status Line: "HTTP/1.1 200 OK" (Success)
            #     - Headers: Specify content type as HTML, UTF-8 encoding
            #     - Blank Line: Separates headers from the body (required by HTTP)
            #     - Body: The actual HTML content to send back
            data = "HTTP/1.1 200 OK\r\n" # Note: HTTP uses \r\n for line endings
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n" # Blank line between headers and body
            data += "<html><body>Hello World</body></html>\r\n\r\n" # Simple HTML body

            # 13. Send the entire HTTP response back to the client
            #     .encode(): Convert the response string back into bytes for sending.
            #     sendall(): Ensures all data is sent (handles potential partial sends).
            client_socket.sendall(data.encode())

            # 14. Signal that the server is done sending data on this connection
            #     SHUT_WR: Shuts down the write direction of the socket.
            #     The client now knows no more data is coming from the server.
            client_socket.shutdown(SHUT_WR)
            # Note: Usually, you'd follow this (or replace it) with client_socket.close()
            # to fully close the connection and release resources immediately. In this
            # simple loop, the 'client_socket' variable gets reused, but explicitly
            # closing is good practice.

    # 15. Handle KeyboardInterrupt (Ctrl+C)
    except KeyboardInterrupt :
        print("\nShutting down...\n")
    # 16. Handle any other exceptions that might occur
    except Exception as exc :
        print("Error:\n")
        print(exc) # Print the details of the error

    # 17. Close the main server listening socket
    #     This happens only when the loop is exited (due to an exception).
    #     It releases the port (9000) so it can be used again.
    server_socket.close()

# 18. Print instructions for accessing the server
print('Access http://localhost:9000')
# 19. Call the function to start the server
create_server()