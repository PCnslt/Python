#!/usr/bin/env python3

import subprocess

interface = input("interface>")
new_mac = input ("new MAC>")

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