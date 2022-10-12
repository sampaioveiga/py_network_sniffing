# Client file
# Estabishes connection and sends default message to server

import socket
import sys

# variables
ip = '127.0.0.1' # server IP address, localhost
port = 8000 # Communication port
buffer_size = 1024

# establish connection
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except OSError as e:
    print('[-] Error creating socket: ' + str(e[0]) + ' - ' + e[1])
    sys.exit();

s.connect((ip, port))

# Sends message to server

try:
    # Type message to server
    msg = input('Message to server: ')
    s.send(msg.encode())
except OSError as e:
    print('[-] Error sending text to server: ' + str(e[0] + ' - ' + e[1]))
    sys.exit()

print('[*] Message sent to server')

# get response from server
data = s.recv(buffer_size)
s.close()
print('[*] Data from server: ' + str(data.decode()))