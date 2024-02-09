# Car script
from can import CanSocket
import socket
from threading import Thread, Timer

# Server Initializing
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 5000))
s.listen(1) # Listening every 1 second
print('Server started')

# CAN interface
can_socket = CanSocket("can0") # Can interface name

def canConnect():
    try:
        can_socket.bind()
    except socket.error as e:
        print(f"Error binding to Can interface: {e}")
        exit(1)

def sendData():
    clientsocket, address = s.accept()
    print(f'Connection from {address} has been established.')
    while True:
        try:
            data = can_socket.recv()
            print(f"Data received from CAN: {data}")
            print(f"Sending message: {data}")
        except socket.error as e:
            print(f"Error receiving CAN message: {e}")

        # Sending data
        clientsocket.send(bytes(data, "utf-8"))

canConnect()
sendData()


