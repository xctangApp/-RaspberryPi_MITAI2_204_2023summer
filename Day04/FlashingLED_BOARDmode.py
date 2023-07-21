import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)

try:
    while True:
        GPIO.output(3, 1)   #turn on the LED
        time.sleep(1)
        GPIO.output(3, 0)   #turn off the LED
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    
