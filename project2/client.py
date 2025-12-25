# import socket

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# client.connect(("127.0.0.0", 8000))


# client.sendall(b"Hello from client")
# data = client.recv(1024)
# print(f"Received from server:", data.decode())

# client.close()

#now let's change the message and see what's happening 
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.0", 8000))


client.sendall(b'/ff/nn/ee')
data = client.recv(1024)
print(f"Received from server:", data.decode())

client.close()
