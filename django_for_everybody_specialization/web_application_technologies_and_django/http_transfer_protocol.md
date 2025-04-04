https://developer.mozilla.org/en-US/docs/Web/HTTP

The Hypertext Transfer Protocol (HTTP) is the foundational protocol for data communication on the World Wide Web. It defines how messages are formatted and transmitted, and what actions web servers and browsers should take in response to various commands. Think of it as the language that web browsers (clients) and web servers use to talk to each other.   

Here's a breakdown of the key concepts of HTTP:

1. Client-Server Model:

Client: Typically a web browser (like Chrome, Firefox, Safari) or any other application that needs to access resources on the web. The client initiates the communication by sending a request.   
Server: A computer that hosts websites and their associated files (HTML documents, images, videos, etc.). The server listens for client requests and sends back responses.   
2. Request-Response Cycle:

HTTP communication follows a request-response cycle:   

Client sends a Request: When you type a website address (URL) into your browser and press Enter, your browser (the client) sends an HTTP request to the web server hosting that website. This request contains information about what the client wants.   
Server receives and processes the Request: The web server receives the request and processes it. This might involve retrieving a file, running a program, or accessing a database.   
Server sends a Response: After processing the request, the server sends an HTTP response back to the client. This response contains the requested resource (e.g., the HTML code of the webpage) along with status information about the request.   
Client receives and processes the Response: The client (browser) receives the response and processes it. For example, if the response contains HTML, the browser will render it to display the webpage to you.   
3. Key Components of HTTP Messages:

Both HTTP requests and responses have a similar structure:

Start Line:
Request: Contains the HTTP method (e.g., GET, POST), the request target (the URL or path), and the HTTP version (e.g., HTTP/1.1, HTTP/2).1 Example: GET /index.html HTTP/1.1   
1.
HTTP messages - MDN Web Docs - Mozilla

developer.mozilla.org

Response: Contains the HTTP version, a status code (indicating the outcome of the request), and a reason phrase (a human-readable description of the status code). Example: HTTP/1.1 200 OK   
Headers: Provide additional information about the request or response. They are key-value pairs. Examples:
Host: www.example.com (Request header indicating the target server)
Content-Type: text/html (Response header indicating the type of data in the body)
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) ... (Request header identifying the client)
  
Body (Optional): Contains the actual data being sent in the request or response. For example:
In a POST request, the body might contain form data.
In a response to a GET request, the body typically contains the requested HTML document, image, or other resource.
4. HTTP Methods (Verbs):

These indicate the action the client wants to perform on the server. Some common HTTP methods include:

GET: Retrieves data from the server (most common).   
POST: Sends data to the server to create or update a resource.
PUT: Updates an existing resource on the server.   
DELETE: Deletes a resource on the server.   
HEAD: Similar to GET, but only retrieves the headers, not the body.   
OPTIONS: Describes the communication options for the target resource.
5. HTTP Status Codes:

These are three-digit codes that the server sends back in the response to indicate the outcome of the request. Common categories include:   

1xx (Informational): The request was received and is being processed.
2xx (Success): The request was successful. (e.g., 200 OK - the request succeeded)   
3xx (Redirection): Further action needs to be taken by the client. (e.g., 301 Moved Permanently - the requested resource has been moved to a new URL)
4xx (Client Error): The client made an error in the request. (e.g., 404 Not Found - the requested resource could not be found)   
5xx (Server Error): The server encountered an error while processing the request. (e.g., 500 Internal Server Error - a generic error occurred on the server)   
6. Stateless Protocol:

HTTP is a stateless protocol. This means that each request from a client to a server is treated as a completely independent transaction. The server does not retain any information about previous requests from the same client. This makes the protocol simple but can sometimes require additional mechanisms (like cookies and sessions) to maintain user state across multiple requests.   

7. Evolution of HTTP:

HTTP/1.1: The most widely used version for a long time. It introduced features like persistent connections to improve performance.   
HTTP/2: Introduced significant performance improvements by allowing multiple requests and responses to be multiplexed over a single TCP connection, as well as header compression.   
HTTP/3: The latest major version, which uses UDP instead of TCP as its transport layer and incorporates QUIC protocol for even better performance and reliability.   
In summary, HTTP is the language of the web, enabling communication between clients (like your browser) and servers to exchange information and deliver the content you see online.   


Sources and related content
