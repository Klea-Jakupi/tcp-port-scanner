import socket
import threading
from queue import Queue
from datetime import datetime

target = input("Enter target IP or domain: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

queue = Queue()
open_ports = []

print("\nScanning started at:", datetime.now())
print("-" * 50)

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
            open_ports.append(port)
            with open("scan_results.log", "a") as log:
                log.write(f"Port {port} is OPEN\n")

        sock.close()

    except socket.error:
        pass

def threader():
    while not queue.empty():
        port = queue.get()
        scan_port(port)
        queue.task_done()

for port in range(start_port, end_port + 1):
    queue.put(port)

for _ in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

queue.join()

print("-" * 50)
print("Scanning finished at:", datetime.now())
print(f"Open ports: {open_ports}")
