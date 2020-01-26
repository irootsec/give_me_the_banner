import socket
import sys

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for host in range(2, 254):
	ports = open('ports.txt', 'r')
	vulnbanners = open('vulnbanners.txt', 'r')	
	conn.settimeout(1)
	for port in ports:
		try:
			conn.connect(( str(sys.argv[1])+'.'+str((host)), int(port) ))
			print ("Conectandose a: {}.{} en el puerto {} ".format(str(sys.argv[1]),str((host)),str((port)))) 
			banner = conn.recv(1024)
			for vulnbanner in vulnbanners:
				if banner.strip() in vulnbanner.strip():
					print ('We have a winner! '+banner)
					print ('Host: '+str(sys.argv[1]+'.'+str(host)))
					print ( 'Port: '+str(port))
		except:
			print ("Error al conectarse a: {}.{} en el puerto {} ".format(str(sys.argv[1]),str((host)),str((port))))