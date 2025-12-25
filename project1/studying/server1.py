import socket

# 1️⃣ Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2️⃣ Bind socket to IP and port
server_socket.bind(("0.0.0.0", 5000))

# 3️⃣ Listen for incoming connections
server_socket.listen(1)
print("[+] Server listening on port 5000")

# 4️⃣ Accept a client connection
client_socket, client_address = server_socket.accept()
print(f"[+] Connection from {client_address}")

# 5️⃣ Receive data from client
data = client_socket.recv(1024)
print(f"[+] Received: {data.decode()}")

# 6️⃣ Send response to client
client_socket.send(b"Hello from TCP server")

# 7️⃣ Close sockets
client_socket.close()
server_socket.close()
