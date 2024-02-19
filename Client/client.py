# Client Script

import socket
import can
import window
import threading

print('Starting Client.')
print('Connecting to server...')

# Server to connect
server = ('rasp5',5000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


gui = None

# Functii pentru modificarea GUI
def inputThrottleData(data):
    global gui
    gui.changeThrottlePercentage(data)

def inputBrakeData(data):
    global gui
    gui.changeBrakePercentage(data)

def inputSpeedData(data):
    global gui
    gui.changeSpeed(data)

def updateData(data):
    # Trebuie cateva IF pentru a verifica ce sa modifica
    inputThrottleData(data)
    inputBrakeData(data)
    inputSpeedData(data)

# Functie pentru pornirea GUI, returneaza gui in variabila
def start_gui():
    global gui
    gui = window.startWindow()

# Functie pentru decodarea mesajului CAN -nu stiu daca e bine :)-
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


# Functie pentru primirea mesajului si decodarea lui
def handle_message():
    while True:
        # 8 sau 12 in functie de can 11/29 cu 11 e bine
        # Receive the CAN message data over the socket connection
        data = s.recv(11).decode('utf-8')

        # Decode the CAN message
        message = decode_can_message(data)

        # If statements pentru fiecare functie care actualizeaza GUI
        #updateData(message)

        # Printing messages received from server
        print(message)



# Folosirea threadurilor pentru a putea actualiza si GUI si a putea primi date simultan
def main():
    # Conencting to server
    s.connect(server)
    gui.statusLabel.setText('Connected to server')

    can_thread = threading.Thread(target=handle_message, args=())
    can_thread.start()
    gui_thread = threading.Thread(target=start_gui, args=())
    gui_thread.start()

main()