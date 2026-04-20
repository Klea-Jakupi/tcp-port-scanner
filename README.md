# tcp-port-scanner
**Multithreaded TCP port scanner in Python**
TCP Port Scanner

**Overview**
This project is a multithreaded TCP port scanner written in Python.
It scans a range of ports on a target system and identifies which ports are open.

**Features**
Multithreaded scanning using Python threading
Queue-based port handling
Timeout for faster scanning
Logs open ports to a file

**How It Works**
The scanner creates multiple threads to scan ports concurrently.
Each thread takes a port from a queue and attempts a TCP connection.
If the connection is successful, the port is marked as open.

**How to Run**
python scanner.py

**What I Learned**
How TCP connections work
Basics of network scanning
Multithreading in Python
Identifying open ports in a system
