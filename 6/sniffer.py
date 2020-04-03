import socket
import struct # libray to convert strings into C structures and vice-versa
import binascii
import sys

try:
    # PF_PACKET for linux, AF_INET for windows and ox800 means IP protocol. 
    raw_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
except OSError as e:
    print('[*] Error creating socket: ' + str(e[0] + ' - ' + e[1]))
    sys.exit()

while True:
    packet = raw_socket.recvfrom(2048)
    print(packet)
    ethernet_header = packet[0][0:14]
    eth_header = struct.unpack("!6s6s2s", ethernet_header)
    print("destination: " + binascii.hexlify(eth_header[0]).decode() + " Source: " + binascii.hexlify(eth_header[1]).decode() + " Type: " + binascii.hexlify(eth_header[2]).decode() )
    ip_header = packet[0][14:34]
    ip_hdr = struct.unpack("!12s4s4s", ip_header)
    print("Source IP: " + socket.inet_ntoa(ip_hdr[1]) + " Destination IP: " + socket.inet_ntoa(ip_hdr[2]) + '\n')