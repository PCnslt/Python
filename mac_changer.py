#!/usr/bin/env python3

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest="interface",help="Name of interface whose MAC address is to be changed.")
    parser.add_option("-m","--mac", dest="new_mac",help="New MAC address.")
    (options,arguments) = parser.parse_args()
    if not options.interface:
        parser.error("Please provide interface name.")
    elif not options.new_mac:
        parser.error("Please provide new MAC address.")
    return options

def change_mac(interface, new_mac):    
    ##One way of using 'subprocess' module
    # subprocess.call("ifconfig",shell=True)
    # subprocess.call("ifconfig "+interface+" down",shell=True)
    # subprocess.call("ifconfig "+interface+" hw ether "+new_mac,shell=True)
    # subprocess.call("ifconfig "+interface+" up",shell=True)
    # subprocess.call("ifconfig "+interface,shell=True)

    ##Another way of using 'subprocess module. Check documentation.
    subprocess.call(["ifconfig"])
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether"+new_mac])
    subprocess.call(["ifconfig",interface,"up"])
    subprocess.call(["ifconfig "+interface])
    
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig",interface])
    # print(ifconfig_result)

    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    print("Search string found: "+mac_address_search_result.group(0))
    
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")

options = get_arguments()
current_mac = get_current_mac(options.interface)
print ("Current MAC = "+str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac==options.new_mac:
    print ("[+] MAC address was successfully changed to: "+current_mac)
else:
    print ("[-] MAC address was not changed: "+current_mac)