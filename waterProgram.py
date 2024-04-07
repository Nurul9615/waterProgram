import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT) # Water Valve
GPIO.setup(17, GPIO.IN) # Moisture Sensor

try:
    while (True):
            if (GPIO.input(17))==0:
                    print('Wet')
                    GPIO.output(18,0)
            elif (GPIO.input(17))==1:
                    GPIO.output(18,1)
                    print('Dry')
            sleep(.25)

finally:
    #cleanup the GPIO pins before ending
    GPIO.cleanup()
