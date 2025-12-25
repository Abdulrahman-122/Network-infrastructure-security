# Socket; software used to connect between server, client
# it's function;
# socket.socket(socket.AF_INET,socket.SOCK_STREAM) => create a socket over the internet
# s.connect_ex((ip,port))  return 0 -> if success else; return failing
# s.bind(("0.0.0.0"),8000) => used by server to attatch ip + port
# s.listen(4) -> put socket into listen mode
# client,addr=s.accept() => accept the incoming connection
# s.sendall("Hello") -> used to send data
# s.recv(1024) -> used to receive data
# s.close() => close the socket
# s.settimeout(1) -> set time for operation

import socket

# 1️⃣ Create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2️⃣ Connect to server
client_socket.connect(("127.0.0.1", 5000))

# 3️⃣ Send message
client_socket.send(b"Hello from TCP client")

# 4️⃣ Receive response
response = client_socket.recv(1024)
print(f"[+] Server says: {response.decode()}")

# 5️⃣ Close socket
client_socket.close()
