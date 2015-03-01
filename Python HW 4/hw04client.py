'''
Erich Chu 
CS 1122 
hw04client.py

Echo Server : Client Code
The way I created an echo server in Python was by creating server code to
start the server and client code to pass the message to the server.
 This is the server portion.
'''

import socket
import sys

#Creates a socket
clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Address and port of the server user wants to connect to
s_address = ('localhost', 10000)
print "Connecting to " + s_address[0] + "port " + str(s_address[1])

#Connects user to the server
clientsock.connect(s_address)

#Inputs message user wants to have echo back
message = raw_input("Enter message \n")

#Sends message to the server
clientsock.sendall(message)

#Receives the echo from the server and prints it
data = clientsock.recv(4096)
print(data)
