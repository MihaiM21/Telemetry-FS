#Script has to run outside the car

import socket
import can
import window
import threading


print('Starting Client.')
print('Connecting to server...')
# Server to connect
server = ('rasp5',5000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(server)

# Data save
throttle_percentage = 0;
brake_percentage = 0;

gui = None
def start_gui():
    global gui
    gui = window.startWindow()
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
def handle_message():
    while True:
        # 8 sau 12 in functie de can 11/29 cu 11 e bine
        # Receive the CAN message data over the socket connection
        data = s.recv(11).decode('utf-8')

        # Decode the CAN message
        message = decode_can_message(data)

        # If statements pentru fiecare functie care actualizeaza GUI


        # Printing messages received from server
        print(message)

def inputThrottleData(data):
    global throttle_percentage
    throttle_percentage = data
    global gui
    gui.changeThrottlePercentage(throttle_percentage)

def inputBrakeData(data):
    global brake_percentage
    brake_percentage = data
    global gui
    gui.changeBrakePercentage(brake_percentage)



def main():
    can_thread = threading.Thread(target=handle_message, args=())
    can_thread.start()
    gui_thread = threading.Thread(target=start_gui, args=())
    gui_thread.start()


main()