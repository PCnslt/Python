#!/usr/bin/env python3

import subprocess

interface = input("interface>")
new_mac = input ("new MAC>")

subprocess.call("ifconfig",shell=True)
subprocess.call("ifconfig "+interface+" down",shell=True)
subprocess.call("ifconfig "+interface+" hw ether "+new_mac,shell=True)
subprocess.call("ifconfig "+interface+" up",shell=True)
subprocess.call("ifconfig "+interface,shell=True)