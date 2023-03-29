import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)
def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def num2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)
    return signal

def new_adc():
    v_dec = 0
    for i in range (0, 8):
        mass = 7 - i
        GPIO.output(dac[i], 1)
        time.sleep(0.01)
        
        compValue = GPIO.input(comp)
        if compValue == 0:
            GPIO.output(dac[i], 0)
        else:
            v_dec = v_dec + 2**mass
    return v_dec
    



try:
    while 1:
        #GPIO.output(dac, 0)
        v_dec = new_adc()
        print(v_dec)
        v = v_dec*3.3/256
        l = int(v/0.5*8)
        
         
        for i in range (0, l + 1):
            
           
            GPIO.output(leds[i], 1)
        for i in range (l + 1, 8):
            
           
            GPIO.output(leds[i], 0)
            time.sleep(0.001)
        print(v)
       
        

finally:
    GPIO.cleanup()
