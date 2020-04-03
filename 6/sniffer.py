import socket
import struct
import binascii
import sys

try:
    # PF_PACKET is linux specific and ox800 means IP protocol
    raw_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
except OSError as e:
    print('[*] Error creating socket: ' + str(e[0] + ' - ' + e[1]))
    sys.exit()

while True:
    packet = raw_socket.recvfrom(2048)
    #print(packet)
    ethernet_header = packet[0][0:14]
    eth_header = struct.unpack("!6s6s2s", ethernet_header)
    #print("destination: " + str(ethernet_header[0]) ) #binascii.hexlify(ethernet_header[0]) )# + " Source: " + str(binascii.hexlify(eth_header[1])) + " Type: " + str(binascii.hexlify(ethernet_header[2])) )
    print("destination: " + str(ethernet_header[0]) + " Source: " + str(eth_header[1]) + " Type: " + str(ethernet_header[2]))
    ip_header = packet[0][14:34]
    ip_hdr = struct.unpack("!12s4s4s", ip_header)
    print("Source IP: " + socket.inet_ntoa(ip_hdr[1]) + " Destination IP: " + socket.inet_ntoa(ip_hdr[2]))