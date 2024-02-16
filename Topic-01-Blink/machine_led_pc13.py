# pyb_led_pc13.py
#
# Copyright (C) 2024 KW Services.
# MIT License
# MicroPython 1.20
#
from machine import Pin
import time

# location of LED
USER_LED_PIN = 'PC13'
# A button connected to pin PB10
USER_BUTTON_PIN = 'PB10'

# Define digital output of builtin LED.
led = Pin(USER_LED_PIN, mode=Pin.OUT)
#user button pulled up to VCC with a resistor
user = Pin(USER_BUTTON_PIN, Pin.IN, Pin.PULL_UP)

done = False

try:
    print("----------------")
    print("Program started.")
    print("* Pin imported from machine module.")
    print("* Using User LED at {}.".format(led))
    print("* User Button defined at {}.".format(USER_BUTTON_PIN))
    print("\n")
    print("Press User button to turn on LED or Control-c in Shell to exit.")
    done = False
    while not done:
        user_btn = user.value()
        if user_btn == 0:
            led.on()
            time.sleep(0.5)
        led.off()
        time.sleep(0.5)
except KeyboardInterrupt:
    done = True
    print('Interrupted by Control-c.')
finally:
    led.off()
    print('Finished.')