import socket

server = "192.168.116.1"
port = 12345

def main():
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((server, port))

  
client.send(b"Hi from client!")
response = client.recv(4096)
print(response.decode())
client.close()

if __name__ == '__main__':
  main()