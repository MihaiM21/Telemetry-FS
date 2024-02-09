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

    userInput = input("Enter something to send or 'q' to quit: ")


while True:
    clientsocket, address = s.accept()
    print(f'Connection from {address} has been established.')
    background_controller(user_input)
    if user_input != '':
        break