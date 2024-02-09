#car script
from can import CanSocket
import socket
from threading import Thread, Timer

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 5000))
s.listen(1) #listening every 1 second
print('Server started')

data = "hau"
user_input = ''
def background_controller(userInput):
    print("Sending: ")
    print(data)
    clientsocket.send(bytes(data, 'utf-8'))
    Timer(1, background_controller).start()


while True:
    clientsocket, address = s.accept()
    print(f'Connection from {address} has been established.')
    background_controller(user_input)