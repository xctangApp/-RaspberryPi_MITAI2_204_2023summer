# LED control from android app
#
#  In this project, a small LED is connected to port GPIO 2 of Raspi
#  The LED is turned ON and OFF from anddroid app
#
#Program:204LEDControl_BT.py
#Date: 07/24/2023
#Author: X.Tang
#

import socket
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LED = 2

GPIO.setup(LED, GPIO.OUT)

GPIO.output(LED, 0)       # turn off the LED to start with

Port = 1
MAC = 'DC:A6:32:8E:0F:3E'
s=socket.socket(socket.AF_BLUETOOTH,socket.SOCK_STREAM,socket.BTPROTO_RFCOMM)
s.bind((MAC, Port))
s.listen(1)
client, addr = s.accept()


try:
    while True:
        data = client.recv(1024)           # Receiving data bytes
        if data.decode('utf-8') == '1':     # 1 received
            GPIO.output(LED, 1)            # LED ON
        elif data.decode('utf-8') == '0':   # 0 received
            GPIO.output(LED, 0)            # LED OFF
            
except KeyboardInterrupt:
    client.close()
    s.close()





