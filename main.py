# Car script TESTING ONLY
import socket
from threading import Thread, Timer

# Server Initializing
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 5000))

def sendData():
    test = True
    clientsocket, address = s.accept()
    print(f'Connection from {address} has been established.')
    while test:
        try:
            # Generate sample CAN message data
            msg_data = {"arbitration_id": 0x123, "data": [0x45, 0x67, 0x89, 0xAB]}
            # Convert the CAN message data to a string
            data_str = ' '.join([f"{b:02x}" for b in msg_data['data']])
            print(f"Data received from CAN: {msg_data['arbitration_id']} {msg_data['data']}")
            print(f"Sending message: {data_str}")

            # Send the CAN message data over the socket connection
            clientsocket.send(bytes(data_str, "utf-8"))
        except socket.error as e:
            print(f"Error sending CAN message data: {e}")
            test = False

def standBy():
    aux = input("Press y to start the server. Press q to quit.")
    if aux == 'y':

        s.listen(5)  # Listening every 1 second
        print('Server started')
        print('Waiting for connection')
        sendData()
    elif aux == 'q':
        exit()

standBy()