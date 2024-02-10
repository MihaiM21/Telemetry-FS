#Script has to run outside the car

import socket
import can

print('Starting Client.')
print('Connecting to server...')
# Server to connect
server = ('rasp5',5000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(server)

def decode_can_message(data):
    message = can.Message(data=bytearray(data[:8]), arbitration_id=int(data[8:16], 16), extended_id=bool(int(data[16], 16)))
    return message
def main():
    while True:
        data = s.recv(1024).decode('utf-8')
        message = decode_can_message(data)
        print(message)
