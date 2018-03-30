#!/usr/bin/env python3
# Moonshine - Proxy SSH connections through a random IP address
# Micah Martin (knif3)

from shine import CONFIG
from shine.tools import *  #addInterface, delInterface, getInterfaceLabels

if __name__ == '__main__':
    #print(addInterface("192.168.58.133"))
    print(delInterface("192.168.58.133"))
    #print(getLabelAddress("eth0:shine77"))
