from machine import Pin as pin, I2C
from utime import sleep
from ssd1306 import SSD1306_I2C

ancho = 128
alto = 64

i2c = I2C(0, scl=pin(22), sda=pin(23))
oled = SSD1306_I2C(ancho, alto, i2c)
led = pin(15, pin.OUT)
led.value(0)

a = pin(33, pin.IN, pin.PULL_UP)
b = pin(32, pin.IN, pin.PULL_UP)
c = pin(26, pin.IN, pin.PULL_UP)
d = pin(25, pin.IN, pin.PULL_UP)

def door_1():

    #led.value(1)
    oled.text("Door 1 open",20,0)
    oled.show()
    sleep(2)


def door_2():

    #led.value(1)
    oled.text("Door 2 open",20,18)
    oled.show()
    sleep(2)


def door_3():

    #led.value(1)
    oled.text("Door 3 open",20,38)
    oled.show()
    sleep(2)


def door_4():
    
    #led.value(1)
    oled.text("Door 4 open",20,55)
    oled.show()
    sleep(2)


def limpiar_pantalla():
    oled.fill(0)
    oled.show()
    #led.value(0)


while True:

    if a.value()==1:      
        door_1()      
    else:       
        limpiar_pantalla()

    if b.value()==1:      
        door_2()      
    else:       
        limpiar_pantalla()

    if c.value()==1:
        door_3()
    else:
        limpiar_pantalla()

    if d.value()==1:
        door_4()
    else:
        limpiar_pantalla()

    led.value(a.value() or b.value() or c.value() or d.value())
