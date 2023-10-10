#!/usr/bin/env python

#Create a queue first: iptables -I FORWARD -j NFQUEUE --queue-num 0
#Install : pip install netfilterqueue
import scapy.all as scapy
import optparse
import netfilterqueue


# def get_arguments():
#     parser = optparse.OptionParser()
#     parser.add_option("-t","--target", dest="target",help="Exact/Range of target IP addresses.")
    
#     (options,arguments) = parser.parse_args()
#     if not options.target:
#         parser.error("Please provide target IP address/range(1/24).")
#     return options

def process_packet(packet):
    print(packet)
    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()

