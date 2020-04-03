# Client file
# Estabishes connection and sends default message to server

import socket
import sys

# variables
ip = '127.0.0.1' # server IP address, localhost
port = 8000 # Communication port
buffer_size = 1024
message_to_send = b'Hi there' # text to send is conveted to bytes

# establish connection
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except OSError as e:
    print('[-] Error creating socket: ' + str(e[0]) + ' - ' + e[1])
    sys.exit();

s.connect((ip, port))

# Sends message to server

try:
    s.send(message_to_send)
except OSError as e:
    print('[-] Error sending text to server: ' + str(e[0] + ' - ' + e[1]))
    sys.exit()

print('[*] Message sent to server')

# get response from server
data = s.recv(buffer_size)
s.close()
print('[*] Data from server: ' + str(data.decode()))