import time, machine
from machine import Pin, I2C
from time import sleep 
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")

arr = [-1, -1, -1]
ledr = Pin(0, Pin.OUT)
ledy = Pin(2, Pin.OUT)
ledg = Pin(4, Pin.OUT)
buttonr = Pin(28, Pin.IN)
buttony = Pin(22, Pin.IN)
buttong = Pin(18, Pin.IN)
x = buttonr.value() 
y = buttony.value() 
z = buttong.value() 
print(buttonr.value())
print(buttony.value())
print(buttong.value())
# countdown = 30 

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

i2c = I2C(0, sda=machine.Pin(20), scl=machine.Pin(21), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS) 

while True: 
    # ledr.value(buttonr.value())
    # ledy.value(buttony.value())
    # ledg.value(buttong.value())
    if(buttonr.value() != x):
        ledr.toggle()
        arr[0] *= -1
        # if(ledr.value()==1):
        #     print("Red led on")
        # else: 
        #     print("Red led off")
        x = buttonr.value()
    if(buttony.value() != y):
        ledy.toggle()
        arr[1] *= -1
        y = buttony.value()
    if(buttong.value() != z):
        arr[2] *= -1
        ledg.toggle()
        z = buttong.value()
    lcd.clear()
    for i in range(3):
        if(arr[i] == 1):
            if(i == 0):
                lcd.putstr("Stop! ")
                sleep(0.1)
            elif i==1:
                lcd.putstr("Wait ")
                sleep(0.1)
            elif i==2: 
                lcd.putstr("Go ")
                sleep(0.1)
    # sleep(0.1)
