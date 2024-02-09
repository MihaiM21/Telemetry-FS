import socket

ip = '192.168.0.104' #ip server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip), 5000)

data = 'test'

def sendData(data):
    s.send(bytes(data, 'utf-8'))

while True:
    print("Sending data...")
    sendData(data)
    print(data)