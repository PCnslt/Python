#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    
    # scapy.arping(ip)
    # scapy.ls(scapy.ARP())
    arp_request = scapy.ARP(pdst = ip)
    # arp_request.pdst = ip
    arp_request.show()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast.show()
    arp_request_broadcast = broadcast/arp_request
    print(arp_request_broadcast.summary())
    arp_request_broadcast.show()

scan("192.168.235.1/24")