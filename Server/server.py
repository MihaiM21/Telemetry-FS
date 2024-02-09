#car script
from can import CanSocket
import socket
from threading import Thread, Timer

#Server Initializing
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 5000))
s.listen(1) #listening every 1 second
print('Server started')

#CAN interface
can_socket = CanSocket("can0")#can interface name

def canConnect():
    try:
        can_socket.bind()
    except socket.error as e:
        print(f"Error binding to Can interface: {e}")
        exit(1)

def sendData():
    while True:
        try:
            message = can_socket.recv()
            print(f"Message received: {message}")
            print(f"Sending message: {message}")
        except socket.error as e:
            print(f"Error receiving CAN message: {e}")

        #sending data
        clientsocket, address = s.accept()
        print(f'Connection from {address} has been established.')
        clientsocket.send(bytes(message, "utf-8"))

#def background_controller(userInput):
 #   print("Sending: ")
  #  print('a')
  #  clientsocket.send(bytes('a', 'utf-8'))
   # Timer(1, background_controller).start()


