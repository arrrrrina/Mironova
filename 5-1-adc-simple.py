import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def num2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)
    return signal

def adc():
    for i in range (0, 256):
        time.sleep(0.001)
        signal = num2dac(i)
        time.sleep(0.1)
        compValue = GPIO.input(comp)
        if compValue == 0:
            return i
            break
        

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

try:
    i = 0

    while 1:
        v_dec = adc()
        v = v_dec*3.3/256
        print(v)
        i+=1

finally:
    GPIO.cleanup()
