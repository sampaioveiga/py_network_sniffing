# Server file
# Listen for connections and waits for message

# variables
import socket
import sys
import threading # server will accept several clients

ip = '127.0.0.1' # server IP address, localhost
port = 8000 # Communication port

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except OSError as e:
    print('[-] Error creating socket: ' + str(e[0]) + ' - ' + e[1])
    sys.exit();

s.bind((ip, port))
s.listen(20) # server accepts 20 clients
print('[*] Listenning...')

# every time a new client connects, server creates a new handler instance
def new_connection_handler(conn):
    buffer_size = 1024
    conn.send(b'[*] Connection accepted')
    while True:
        data = conn.recv(buffer_size)
        print('[*] Message from client: ' + str(data.decode())) # data received is converted from bytes to string
        if not data:
            break
        conn.sendall(b'[*] Received')
    conn.close()

# accepts connetions from clients
while True:
    conn, addr = s.accept()
    print('[*] Connection from ' + str(addr) + ' accepted')

    # each client will spawn a new thread 
    x = threading.Thread(target=new_connection_handler, args=(conn,))
    x.start()
s.close()