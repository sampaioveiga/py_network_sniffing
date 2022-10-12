import socket

# server config
host = "0.0.0.0"  # listen on all interfaces
port = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP socket
print ("Socket created successfully")

server.bind((host, port))
server.listen(5)
print (f"[*] Server is listening")

while True:
  conn, addr = server.accept()
  print (f"[*] Connected from ", addr)

  conn.send(b"[*] Hi. You're now connected.\n")
  conn.close()

  break     # break and exit