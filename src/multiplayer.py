import socket
import sys

def listen(addr, port):
	print addr
	print port
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((addr,port))
	s.listen(5)
	while True:
		#try:
		c, addr = s.accept()
		print c.recv(1024)
		c.send("ACK SENT BY SERVER")
		c.close()
		#except:
		#	pass
	
	
def send(addr, port, dest, dest_port):
	print addr, port, dest, dest_port
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((addr,port))
	s.connect((dest, dest_port))
	s.send("TEST CLIENT MESSAGE FROM CLIENT")
	print s.recv(1024)
	s.close()
	
if sys.argv[1] == "client":
	send(sys.argv[2], int(sys.argv[3]), sys.argv[4], int(sys.argv[5]))
else:
	listen(sys.argv[2], int(sys.argv[3]))
	

	
	
	

