# Car script
import socket
from threading import Thread, Timer
from requests import packages
import can

# Server Initializing
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 5000))

# Create a CAN interface using the socketcan backend
can_interface = can.Bus(bustype='socketcan', channel='can0')

def sendData():
    clientsocket, address = s.accept()
    print(f'Connection from {address} has been established.')
    while True:
        try:
            # Read a message from the CAN bus
            msg = can_interface.recv(1)
            if msg:
                # Convert the CAN message to a string
                data = f"{msg.arbitration_id:08x} {msg.data.hex()}"
                print(f"Data received from CAN: {data}")
                print(f"Sending message: {data}")

                # Send the CAN message over the socket connection
                clientsocket.send(bytes(data, "utf-8"))
            else:
                print("No CAN message received")
        except socket.error as e:
            print(f"Error receiving CAN message: {e}")

        except can.CanError as e:
            print(f"Error receiving CAN message: {e}")

def standBy():
    aux = input("Press y to start the server. Press q to quit.")
    if aux == 'y':

        s.listen(1)  # Listening every 1 second
        print('Server started')
        print('Waiting for connection')
        sendData()
    elif aux == 'q':
        exit()

standBy()