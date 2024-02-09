import socket
from threading import Thread, Timer

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 5000))
s.listen(1) #listening every 1 second
print('Server started')

def background_controller():
    message = 'Hello client'
    print(message)
    clientsocket.send(bytes(message, 'utf-8'))
    Timer(1, background_controller).start()

def receiveData():
    print(s.recv(1024).decode('utf-8'))

while True:
    clientsocket, address = s.accept()
    print(f'Connection from {address} has been established.')
    #background_controller()
    receiveData()