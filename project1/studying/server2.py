# Create a socket code using UDP to fast connection between client,server
# it's connectionless
# it's not flow controlled
# it's not guarntee

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("0.0.0.0", 5001))
print("UDP server listen on port 5001:")

while True:
    data, client_address = server.recvfrom(1024)
    print(f"Received from {client_address}:", data.decode())
    server.sendto(b"Hello form UDP server", client_address)
