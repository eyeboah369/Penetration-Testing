import sys
import ipaddress
from netaddr import *
import pprint

ip = IPAddress('000.000.000.000')   #add appropriate IP Address
print("The IP version of the IP Address is: " + str(ip.version))

ip = IPNetwork('000.000.000.000')   #add appropriate IP Address
print("This is the ip value: " + str(ip.value))

print("This is the IP Network: " + str(ip.network))
print("This is the IPs broadcast: " + str(ip.broadcast))
print(ip.size)
print(ip.netmask)
print(ip.hostmask)
