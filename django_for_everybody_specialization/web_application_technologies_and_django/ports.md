Ports are communication endpoints in a network used for managing data traffic between devices. They allow different services and applications to communicate over a network by assigning a unique number to each service or protocol. These port numbers help computers identify which program or service should handle incoming or outgoing data. Ports are used in both TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) connections, which are the most common protocols for network communication.

Here’s a breakdown of how ports work and the different types of port numbers:

Port Number Ranges:
Ports are numbered from 0 to 65535, and they are divided into three categories:

Well-known Ports (0-1023):

These are reserved for widely-used and standard network protocols, like HTTP, FTP, SMTP, etc.

These ports are typically assigned to core services and are usually required to run with elevated privileges (i.e., administrative rights) on a computer or device.

Examples:

Port 80 – HTTP (Hypertext Transfer Protocol)

Port 443 – HTTPS (HTTP Secure)

Port 21 – FTP (File Transfer Protocol)

Port 22 – SSH (Secure Shell)

Registered Ports (1024-49151):

These are used by software applications for specific purposes. They are registered by software vendors to avoid conflicts between different applications.

While not as widely used or standardized as well-known ports, many popular applications and services use these ports.

Examples:

Port 3306 – MySQL Database

Port 8080 – Often used as an alternative HTTP port for web servers

Port 1433 – Microsoft SQL Server

Dynamic or Private Ports (49152-65535):

These are temporary ports often used by client applications during communication with servers. These ports are dynamically assigned and are used for the duration of a session.

Typically, the operating system assigns these ports when an application requests one for outbound communication.

Example: When you visit a website, your browser uses a dynamically assigned port (such as 49152) to communicate with the server on port 80 (HTTP) or 443 (HTTPS).

TCP vs. UDP Ports:
Both TCP and UDP use port numbers to identify the service or application they communicate with, but the key difference lies in how the two protocols handle communication.

TCP Ports:

TCP (Transmission Control Protocol) is a connection-oriented protocol, meaning it establishes a reliable connection between the sender and receiver. It ensures that data is delivered correctly, and the order is preserved.

Ports in TCP are used for services like HTTP, FTP, SSH, and many others.

Example:

Port 80 – HTTP (for web browsing)

Port 443 – HTTPS (secure web browsing)

UDP Ports:

UDP (User Datagram Protocol) is a connectionless protocol. It sends data without establishing a reliable connection, making it faster but less reliable than TCP. It’s often used in real-time applications like video streaming or online gaming where speed is prioritized over reliability.

Ports in UDP are used for services like DNS, NTP, and streaming services.

Example:

Port 53 – DNS (Domain Name System) – used to resolve domain names into IP addresses

Port 123 – NTP (Network Time Protocol) – used to synchronize time across networks

Common Ports and Their Uses:
Here’s a list of some common ports and the services they’re associated with:

Port Number	Protocol	Service
20, 21	TCP	FTP (File Transfer Protocol)
22	TCP	SSH (Secure Shell)
23	TCP	Telnet
25	TCP	SMTP (Simple Mail Transfer Protocol)
53	UDP/TCP	DNS (Domain Name System)
67, 68	UDP	DHCP (Dynamic Host Configuration Protocol)
80	TCP	HTTP (Hypertext Transfer Protocol)
110	TCP	POP3 (Post Office Protocol 3)
143	TCP	IMAP (Internet Message Access Protocol)
443	TCP	HTTPS (Hypertext Transfer Protocol Secure)
3306	TCP	MySQL
3389	TCP	RDP (Remote Desktop Protocol)
Why Ports Matter:
Data Routing: Ports help routers and firewalls determine where to send data. When data packets are sent over the internet, they include both the destination IP address (where to send the data) and the port number (which application or service should handle it).

Security: Because certain ports are associated with specific services, attackers may try to exploit vulnerabilities in services running on those ports (e.g., port 22 for SSH). Network security tools like firewalls can filter traffic based on port numbers to protect against such attacks.


Common TCP Ports:
Port 80 – HTTP (Hypertext Transfer Protocol) – Used for web traffic.

Port 443 – HTTPS (HTTP Secure) – Used for secure web traffic.

Port 21 – FTP (File Transfer Protocol) – Used for file transfers.

Port 22 – SSH (Secure Shell) – Used for secure remote logins and file transfers.

Port 23 – Telnet – Used for unencrypted remote communication (not recommended due to lack of security).

Port 25 – SMTP (Simple Mail Transfer Protocol) – Used for sending emails.

Port 109 – POP2 (Post Office Protocol version 2), an older email retrieval protocol (now largely deprecated).

Port 110 – POP3 (Post Office Protocol 3) – Used for retrieving emails.

Port 143 – IMAP (Internet Message Access Protocol) – Used for accessing and managing emails on a remote server.

Port 3306 – MySQL – Used by MySQL databases for client-server communication.

Port 3389 – RDP (Remote Desktop Protocol) – Used for remote desktop connections on Windows.

Common UDP Ports:
Port 53 – DNS (Domain Name System) – Used for resolving domain names into IP addresses.

Port 67 – DHCP (Dynamic Host Configuration Protocol) – Used for network devices to receive IP addresses automatically.

Port 161-162 – SNMP (Simple Network Management Protocol) – Used for network management.

Port 69 – TFTP (Trivial File Transfer Protocol) – A simplified version of FTP.

Port 123 – NTP (Network Time Protocol) – Used for time synchronization between devices.

Port 161 – SNMP (Simple Network Management Protocol) – Used for network management (also used for receiving SNMP traps).

Port 514 – Syslog – Used for sending log and event messages between devices.

Other Notable Ports:
Port 53 (DNS) – Both UDP and TCP are used for DNS queries. UDP is used for the majority of queries, while TCP is used for larger responses.

Port 514 (Syslog) – Primarily uses UDP for log messages.