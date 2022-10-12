import socket
import sys

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print ("Socket created")
except socket.error as err:
	print ("socket creation failed with error %s" %(err))

# default port for socket
port = 80

try:
	host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:

	print ("there was an error resolving the host")	# could not resolve hostname, quit
	sys.exit()

# connecting to the server
s.connect((host_ip, port))

print ("The socket has successfully connected to google")
