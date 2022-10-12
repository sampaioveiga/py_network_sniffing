# Server file
# Listen for connections and waits for message

# variables
import socket
import sys

ip = '127.0.0.1' # server IP address, localhost
port = 8000 # Communication port
buffer_size = 1024

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except OSError as e:
    print('[-] Error creating socket: ' + str(e[0]) + ' - ' + e[1])
    sys.exit();

s.bind((ip, port))
s.listen(1) # server accepts 1 client
print('[*] Listenning...')

# accepts connetions from client
while True:
    conn, addr = s.accept()
    print('[*] Connection from ' + str(addr) + ' accepted')
    conn.send(b'Connection accepted')
    data = conn.recv(buffer_size)
    print('[*] Message from client: ' + str(data.decode())) # data received is converted from bytes to string
    conn.close()
s.close()