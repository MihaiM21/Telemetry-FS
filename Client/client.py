import socket

ip = '192.168.0.59' #ip server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip), 5000)

data = 'test'

def sendData(data):
    s.send(bytes(data, 'utf-8'))

while True:
    print(s.recv(1024).decode('utf-8'))