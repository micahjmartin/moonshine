#!/usr/bin/env python3
# Moonshine - Proxy SSH connections through a random IP address
# Micah Martin (knif3)

from shine import CONFIG
from shine.iproute2 import *  #addInterface, delInterface, getInterfaceLabels

if __name__ == '__main__':
    delRoute("10.90.100.2")
    #label = addInterface("192.168.58.133")
    #delInterface("192.168.58.133")
