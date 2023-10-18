#!/usr/bin/env python

#Create a queue for other computer: iptables -I FORWARD -j NFQUEUE --queue-num 0
#Create a queue for own computer: iptables -I OUTPUT -j NFQUEUE --queue-num 0
#Create a queue for own computer: iptables -I INPUT -j NFQUEUE --queue-num 0
#Install : pip install netfilterqueue

import netfilterqueue
import scapy.all as scapy


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        print(scapy_packet.show)
    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(1, process_packet)
queue.run()

