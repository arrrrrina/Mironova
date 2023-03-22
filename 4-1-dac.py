import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(dac, GPIO.OUT)


def dec2bin(val):
    return [int(element) for element in bin(val)[2:].zfill(8)]

def ischislo(num):
    flag = 1
    a = "-.1234567890"
    for i in num:
        if (a.find(i) != -1):
            flag *= 1
        else:
            flag *= 0
    
    if (flag):
        return 1
    
    return 0

def isint(num):
    flag = 1
    a = "-1234567890"
    for i in num:
        if (a.find(i) != -1):
            flag *= 1
        else:
            flag *= 0
    
    if (flag):
        return 1
    
    return 0

try:
    while(True):
        num = input('Enter number from 0 to 255:')
        if (num == 'q'):
            break
        else:
            if (not (ischislo(num))):
                print("not a number")
                break
            elif ( not (isint(num))):
                print("ne celoe")
                break
            elif (int(num) < 0):
                print("less zero")
                break
            elif (int(num) > 255):
                print("too big")
                break

            num = int(num)
            GPIO.output(dac, dec2bin(num))
            u = 3.3 * (float(num) / 256.0)
            print('Voltage is ', u)
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()