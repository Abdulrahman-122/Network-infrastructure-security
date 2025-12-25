# UDP client
# send data to UDP server

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b"Hello from UDP client", ("127.0.0.1", 5001))
data, server = client.recvfrom(1024)
print(f"Received from UDP server : {data.decode()}")
client.close()
