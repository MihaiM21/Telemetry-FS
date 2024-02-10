#Script has to run outside the car

import socket
import can
import binascii

print('Starting Client.')
print('Connecting to server...')
# Server to connect
server = ('rasp5',5000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(server)

def decode_can_message(data):
    # Remove spaces from the data string
    data = data.replace(' ', '')

    # Extract the CAN message data and arbitration ID from the received byte string
    arbitration_id = int(data[:6], 16)
    data_str = data[7:].strip()
    dlc = len(data_str) // 2
    data = [int(data_str[i:i + 2], 16) for i in range(0, len(data_str), 2)]

    # Create a new CAN message using the extracted data and ID
    message = can.Message(arbitration_id=arbitration_id, data=data)
    return message
def main():
    while True:
        # 8 sau 12 in functie de can 11/29 cu 11 e bine
        # Receive the CAN message data over the socket connection
        data = s.recv(11).decode('utf-8')

        # Decode the CAN message
        message = decode_can_message(data)
        print(message)

main()