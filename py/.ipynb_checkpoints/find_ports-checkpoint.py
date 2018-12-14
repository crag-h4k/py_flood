from bat import bro_log_reader

def find_orig_ports(log,flags):
    reader = bro_log_reader.BroLogReader(log)
    ports = []
     
    for row in reader.readrows():
        for flag in flags:
            if (flag) in (row['server_name'] or row['subject']):
                ports.append(row['id.orig_p'])

    ordered = sorted(ports)
    return [ordered[0],ordered[-1]]


if __name__ == '__main__':
    log = '../test_2/ssl.log'
    ports = find_orig_ports(log,['lol','riot'])
    print(ports)
