'''
Erich Chu 
CS 1122 
hw04server.py 

Echo Server: Server Code
The way I created an echo server in Python was by creating server code to
start the server and client code to pass the message to the server.
 This is the server portion.
'''

import socket
import sys

#Creates a socket
serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Address and port of the server being created
s_address = ('localhost', 10000)
print "Starting server on " + s_address[0] + "port " + str(s_address[1])

#Socket is now associated with the address and port
serversock.bind(s_address)

#Listen for any incoming connections
serversock.listen(5)

while True:
	#Wait till a connection is received
    print "Searching for connection..."

    #Retrieve connection socket
    con, addr = serversock.accept()

    #Receive message from client
    data = con.recv(4096)
    print "Received and sent: " + data

    #Send back the message (AKA echo back) to the client
    con.sendall(data)

