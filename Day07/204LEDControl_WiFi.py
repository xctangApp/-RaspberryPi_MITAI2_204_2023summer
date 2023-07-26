# LED control from android app
#
#  In this project, a small LED is connected to port GPIO 2 of Raspi
#  The LED is turned ON and OFF from anddroid app
#
#Program:204LEDControl_WiFi.py
#Date: 07/25/2023
#Author: X.Tang
#

from flask import Flask, render_template
import RPi.GPIO as GPIO

app=Flask(__name__)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LED = 2
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, 0)

#
#  start of the main program loop, read commands from the android device,
#  decode the message and control LED
#

@app.route("/<device>/<action>")
def action(device, action):
    actuator = LED
    if action == "on":
        GPIO.output(actuator, GPIO.HIGH)
    if action == "off":
        GPIO.output(actuator, GPIO.LOW)
    return ""

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0', use_reloader=False)


