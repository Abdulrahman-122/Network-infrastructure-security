import socket
from datetime import datetime

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 8000))
server.listen(1)
print(f"Server now listen on port 8000:")

while True:
    client, addr = server.accept()
    print(f"Received data from:{addr}")       #address here return ; ip address of client, sequence number (random)
    data = client.recv(1024)
    if not data:
        client.close()
        continue
    message = f"Received data from client:{data.decode(errors='ignore')}"     

    with open("logs.txt", "a") as log:
        log.write(f"{datetime.now()} | {addr[0]}|{message} \n")

    client.sendall(b"Message received.")
    client.close()
