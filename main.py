# Car script
import socket
from threading import Thread, Timer

# Server Initializing
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 5000))
s.listen(1) # Listening every 1 second
print('Server started')

def sendData():
    clientsocket, address = s.accept()
    print(f'Connection from {address} has been established.')
    while True:
        try:
            # Generate sample CAN message data
            msg_data = {"arbitration_id": 0x123, "data": [0x45, 0x67, 0x89, 0xAB]}
            # Convert the CAN message data to a string
            data_str = ' '.join([f"{b:02x}" for b in msg_data['data']])
            print(f"Data received from CAN: {data_str}")
            print(f"Sending message: {data_str}")

            # Send the CAN message data over the socket connection
            clientsocket.send(bytes(data_str, "utf-8"))
        except socket.error as e:
            print(f"Error sending CAN message data: {e}")
            break

sendData()