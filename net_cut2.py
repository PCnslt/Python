#!/usr/bin/env python

#Create a queue first: iptables -I FORWARD -j NFQUEUE --queue-num 0
#Install : pip install netfilterqueue
import scapy.all as scapy
import optparse
import netfilterqueue 


def print_and_accept(pkt):    
    print(pkt)
    pkt.accept()

nfqueue = netfilterqueue.NetfilterQueue()
nfqueue.bind(1, print_and_accept)
try:
    nfqueue.run()
except KeyboardInterrupt:
    print('')

nfqueue.unbind()