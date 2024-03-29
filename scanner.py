#!/bin/python3

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
	print("Invalid amount of arguments")
	print("Syntax: python3 scanner.py <ip>")

#Add a banner
print("-" * 50)
print("Scanning Target "+target)
print("Time started: " +str(datetime.now()))
print("-" * 50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET means IPv4, SOCK_STREAM means port
		socket.setdefaulttimeout(1) #Can be adjusted in length for either speed or accuracy 
		result = s.connect_ex((target,port)) #returns error indicator
		if result == 0:
			print("Port {} is open".format(port))
		s.close()

except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved")
	sys.exit()

except socket.error:
	print("Couldn't connect to server")
	sys.exit()


