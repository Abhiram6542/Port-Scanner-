import sys
import socket
from datetime import datetime

#define our Target 

if len(sys.argv) == 2:
		target = socket.gethostbyname(sys.argv[1]) #Translate to hostname to ipv4
else:
	print("Invalid  amount of argument")
	print("Syntax:python3 scanner.py <ip>")

#Add a pretty banner 

print("-" * 50)
print("Scanning Target"+target)
print("Time Started:"+str(datetime.now()))
print("-" * 50)


try:
	for port in range(50,888):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(0.5)
		result=s.connect_ex((target,port)) #return an arror indicator
		if result == 0:
			print("Port {} is open".format(port))
		s.close()

except KeyboardInterrupt:
	print("\nExiting Progarme.")
	sys.exit()
except socket.gaierror:
	print("Hostname Could Not Resolve ")
	sys.exit()
except socket.error:
	print("Could't connect to server")
	sys.exit()
