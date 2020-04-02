# Server file
# Estabishes connection and waits for message

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

# gets port and waits

s.bind((ip, port))
s.listen(1) # listen for incomming connections - limited to 1
print('[*] Listenning...')

while True:
    # accepts connetions, prints message and acknowledges
    conn, addr = s.accept()
    print('[*] Connection from ' + str(addr) + 'accepted')

    data = conn.recv(buffer_size)
    print('[*] Message from client: ' + str(data.decode())) # data received is converted from bytes to string

    conn.send(b'[*] Received. Over and Out')

conn.close()