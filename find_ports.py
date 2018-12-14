from datetime import datetime
from pprint import pprint

from bat import bro_log_reader
from cfg import SSL_LOG, FLAGS


class Target:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.ts = datetime.now()

def find_traffic(log,flags):
    reader = bro_log_reader. BroLogReader(log)
    traffic = []
     
    for row in reader.readrows():
        for flag in flags:     
            if (flag) in (row['server_name'] or row['subject']):
                traffic.append({'ip':row['id.orig_h'],'port':row['id.orig_p']})
    #print(sorted(traffic, key= lambda k: k['ip']))
    return sorted(traffic, key= lambda k: k['ip'])

def sort_ips(sorted_traffic):
    ips = [] 
    for conn in sorted_traffic:
        if conn['ip'] not in ips:
            ips.append(conn['ip'])
    print(ips)
    return ips

def make_targets(sorted_traffic, ip_list):
    targets = []
    ports = []
    for ip in ips:
        for conn in sorted_traffic:
            if ip == conn['ip']: ports.append(conn['port'])
        p_sorted = sorted(ports)
        T = Target(ip, [p_sorted[0],p_sorted[-1]])
        targets.append(T)
    print(targets)
    return targets
    #return{'ip':p_sorted[0].get('ip'), 'port_range':[p_sorted[0].get('port'),p_sorted[-1].get('port')]}

if __name__ == '__main__':
    conns = find_traffic(SSL_LOG,FLAGS)
    ips = sort_ips(conns)
    targets = make_targets(conns, ips)
    for i in targets:
        print('IP: ', i.ip)
        print('Port: ', i.port)
