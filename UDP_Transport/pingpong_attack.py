#!/bin/env python3

from scapy.all import *

ip   = IP(src="192.168.44.131", dst="192.168.44.129")
udp  = UDP(sport=9090, dport=9090)
data = "Let the Ping Pong game start!\n"
pkt  = ip/udp/data
send(pkt, verbose=0)