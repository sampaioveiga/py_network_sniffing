import socketserver

# RequestHandler class
class TCPRequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data.decode())

        self.request.sendall(self.data)

# create server, bind localhost to port 8000 and create class instance
server = socketserver.TCPServer(("", 8000), TCPRequestHandler)
print("[*] listenning...")

# keep server running
server.serve_forever()