import random
import board
import neopixel
import time
import RPi.GPIO as GPIO
import gpiozero as IOZ
from gpiozero import PWMLED
from signal import pause
import sys

pixels = neopixel.NeoPixel(board.D18, 16)

button = IOZ.Button("BOARD29", pull_up=False)
button_two = IOZ.Button("BOARD32", pull_up=False)

status = False

def randrgb():
    return random.randint(1, 255)

#run()


def main():
    status = False
    while True:
            if button_two.is_pressed:
                r = randrgb()
                b = randrgb()
                g = randrgb()
                for i in range(16):
                    pixels[i] = (r,g,b)
            if button.is_pressed:
                if status == False:
                    status = True
                else:
                    status = False
            if status == True:
                for i in range(16):
                    pixels[i] = (255,0,0)
            else:
                for i in range(16):
                    pixels[i] = (0,0,0)
                    
def led_on():
    global status
    status = True
    
def led_off():
    global status
    status = False
    
def rand_color():
    global color
    color = (random.randrange(255), random.randrange(255), random.randrange(255))
    

color = (255,0,0)    
        
def main2():
    global status
    global color
    while True:
        if status==False:
            button.when_released = led_on
        else:
            button.when_released = led_off
            
        button_two.when_released = rand_color
            
        if status == True:
            for i in range(16):
                pixels[i] = color
        else:
            for i in range(16):
                pixels[i] = (0,0,0)    
    
        
main2()


              
                
                    





