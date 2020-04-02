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

conn, addr = s.accept()
print('[*] Connection from ' + str(addr) + ' accepted')

while True:
    command = input('$ ')
    conn.send(command.encode())
    if str(command) == 'exit':
        conn.close()
        break
    print(conn.recv(buffer_size))
s.close()