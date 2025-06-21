#Sender script

import serial
import time

#Use one end of the virtual COM pair.
ser = serial.Serial('COM9', 9600)

try:
  while True:
    message = "Hello, Cansat!\n"
    ser.write(message.encode('utf-8'))
    print(f"Sent: {message.strip()}")
    time.sleep(1)
except KeyboardInterrupt:
  ser.close()
  print("Sender stopped.")


#This script will send, "Hello, Cansat!" every second to COM3 (simulating ESP32)