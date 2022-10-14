import socket
import threading

# server config
host = "0.0.0.0"
port = 12345

def main():
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind((host,port))
  server.listen(5)
  print(f"[*] Server is listenning")

  while True:
    client, address = server.accept()
    print(f"[*] Connection accepted from {address[0]}:{address[1]}")
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()

def handle_client(client_socket):
  with client_socket as sock:
    request = sock.recv(1024)
    print(f"[*] Received: {request.decode('utf-8')}")
    sock.send(b"[*] ACK")

if __name__ == '__main__':
  main()