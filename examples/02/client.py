import socket

server = "192.168.116.1"
port = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((server, port))

response = client.recv(4096)
print(response.decode())

client.close()