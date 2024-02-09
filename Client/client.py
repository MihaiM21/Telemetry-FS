#Script has to run in

import socket

ip = '192.168.0.59' #ip server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('rasp5', 5000))


while True:
    print(s.recv(1024).decode('utf-8'))