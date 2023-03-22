import RPi.GPIO as GPIO
import time as t

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(dac, GPIO.OUT)

def dec2bin(val):
    return [int(element) for element in bin(val)[2:].zfill(8)]

try:
    num = 0
    flag = 0
    while (True):
        if (num < 255 and flag == 0):
            num += 1
        elif (num > 0):
            num -= 1
            flag = 1
        elif (num == 0):
            flag = 0

        GPIO.output(dac, dec2bin(num))
        
        sec = 5.0
        t.sleep(sec / 512.0)
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()