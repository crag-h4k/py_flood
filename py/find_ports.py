from bat import bro_log_reader

def find_traffic(log,flags):
    reader = bro_log_reader.BroLogReader(log)
    traffic = []
     
    for row in reader.readrows():
        for flag in flags:
            if (flag) in (row['server_name'] or row['subject']):
                traffic.append({'host':row['id.orig_h'],'port':['id.orig_p']})
    
    # add grouping of hosts here

    ordered = sorted(traffic, key= lambda k: k['port'])
    return{'ip':ordered[0].get('host'), 'port_range':[ordered[0].get('port'),ordered[-1].get('port')]}


if __name__ == '__main__':
    log = '../test_2/ssl.log'
    ports = find_orig_ports(log,['lol','riot'])
    print(ports)
