import  RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

GPIO.setmode(GPIO.BCM)
#------------------------------------
leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(17, GPIO.IN)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

#--------------------------------------
def dec2bin(val):
    return [int(element) for element in bin(val)[2:].zfill(8)]

def output_leds(num):
    GPIO.output(leds, dec2bin(num))

def num2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)
    return signal

def adc():
    mass = [0] * 8
    value = 0
    for i in range (7, -1, -1):
        mass[i] = 1
        GPIO.output(dac, mass)
        time.sleep(0.001)
        mass[i] = GPIO.input(comp)
        value += mass[i]**2**i
    return value
        
try:
    GPIO.output(17, 1)
    data = []
    begin = time.time()
    
    v = 0

    #----------(зарядка)----------------
    while v < 3:
        num = adc()
        data.append(num)
        v = num * 3.3 / 256
        print(v)
        output_leds(num)
    
    # #----------(разрядка)---------------
    # GPIO.output(17, 0)
    # v = get_voltage()
    # while v > 0.1:
    #     data.append(v)
    #     v = get_voltage()
    #     num = int(v/3.3*256)
    #     print (v)
    #     output_leds(num)

    end = time.time()

    plt.plot(data)
    plt.show()

finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()
