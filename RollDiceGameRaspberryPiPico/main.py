import time, random
from machine import Pin, ADC, I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from time import sleep 
time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")
print("A simulation game")

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

i2c = I2C(0, sda=machine.Pin(20), scl=machine.Pin(21), freq=400000)
lcd = I2cLcd(i2c, 0x27, 4, 20)    

pot = ADC(26)
sevenseg1 = [0,1,2,3,4,5,6]
# ledss1a = Pin(0, Pin.OUT)
# ledss1b = Pin(1, Pin.OUT)
# ledss1c = Pin(2, Pin.OUT)
# ledss1d = Pin(3, Pin.OUT)
# ledss1e = Pin(4, Pin.OUT)
# ledss1f = Pin(5, Pin.OUT)
# ledss1g = Pin(6, Pin.OUT)
# ledss1 = [ledss1a, ledss1b, ledss1c, ledss1d, ledss1e, ledss1f, ledss1g]
ledss1 = []

sevenseg2 = [7,8,9,10,11,12,13]
ledss2 = []
ledss = [ledss1, ledss2]

data = [
    [0,1,1,0,0,0,0],
    [1,1,0,1,1,0,1], 
    [1,1,1,1,0,0,1],
    [0,1,1,0,0,1,1],
    [1,0,1,1,0,1,1],
    [1,0,1,1,1,1,1]
]

for i in range(7):
    ledss1.append(Pin(sevenseg1[i], Pin.OUT))
    ledss2.append(Pin(sevenseg2[i], Pin.OUT))

def fn2(k, idx):
    for i in range(6):
        if(i == idx-1):
            for j in range(7):
                ledss[k][j].value(data[i][j])

while True: 
    num1 = random.randrange(1, 7)
    num2 = random.randrange(1, 7)
    # fn2(0, num1)
    # fn2(1, num2)
    pot_value = pot.read_u16()  #0 to 65535
    val = pot_value/65535
    if val <= 0.33:
        lcd.putstr("Roll the dice")
    elif val > 0.33 and val <= 0.67: 
         fn2(0, num1)
         lcd.clear()
         lcd.putstr("Dice 1: " + str(num1))
         lcd.move_to(0, 1)
         lcd.putstr("Roll dice 2!")
    else: 
        fn2(0, num1)
        fn2(1, num2)
        lcd.clear()
        lcd.putstr("Dice1: " + str(num1) + "Dice2: " + str(num2))
        lcd.move_to(0, 1)
        if num1 == num2:
            lcd.putstr("You Won!")
            break
        else: 
            lcd.putstr("Try Again!")
    # lcd.putstr(str(num1) + " " + str(num2))
    # lcd.putstr(str(pot_value))
    # print(num1)
    # print(num2)
    sleep(1)
    lcd.clear()


