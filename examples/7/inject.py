import socket
import struct
import sys

try:
    s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x800))
except OSError as e:
    print('[*] Error creating socket: ' + str(e[0] + ' - ' + e[1]))
    sys.exit()

# now bind socket to an interface - run 'ip link' to list computer interfaces and replace wlp2s0
s.bind(('wlp2s0', socket.htons(0x800)))

packet = struct.pack("!6s6s2s", '\xb8v?\x8b\xf5\xfe', '1\x19\x8f\xe1J\x8c', '\x08\x00')
s.send(packet)#  + 'I\'m here')