import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

def dec2bin(val):
    return [int(element) for element in bin(val)[2:].zfill(8)]

#dac = [26, 19, 13, 6, 5, 11, 9, 10]

t = 0
p = GPIO.PWM(18, 10000)
p.start(0)
try:
    while t != 101:
        #dec = int(input'Enter number from 1 to 255')
        #GPIO.output(dac, dec2bin(dec))

        t = int(input('Enter duty cycle: '))
        if t == 101:
            p.stop()
            break
        if t >= 0 and t < 101:
            p.ChangeDutyCycle(t)
            print(t/100*3.3)
        else:
            print('Wrong size of duty cycle')

finally:
    GPIO.cleanup()
