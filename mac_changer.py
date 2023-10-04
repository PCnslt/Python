#!/usr/bin/env python3

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest="interface",help="Name of interface whose MAC address is to be changed.")
    parser.add_option("-m","--mac", dest="new_mac",help="New MAC address.")
    return parser.parse_args()

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
    

(options,arguments) = get_arguments()

change_mac(options.interface, options.new_mac)