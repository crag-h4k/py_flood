from flood import udp_flood
from find_ports import find_orig_ports
from cfg import SSL_LOG, FLAGS

port_range = find_traffic(SSL_LOG, FLAGS)

