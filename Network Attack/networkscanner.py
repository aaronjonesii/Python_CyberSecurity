"""
Function:       				Multi-Thread Port Scanner
Created Date:           02.09.2019
Updated Date:						06.07.2021
Created By:     				Anonymous Systems (0_o)
Dependencies:						None
Reference:							https://stackoverflow.com/questions/207234/list-of-ip-addresses-hostnames-from-local-network-in-python

TODO:
Determine your own IP address
Determine your own netmask
Determine the network range
Scan all the addresses (except the lowest, which is your network address and the highest, which is your broadcast address).
Use your DNS's reverse lookup to determine the hostname for IP addresses which respond to your scan.

"""

class NetworkScanner():
	def __init__(self)
