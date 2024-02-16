# pyb_LED.py
#
# Copyright (C) 2024 KW Services.
# MIT License
# MicroPython 1.20
#
from pyb import Pin, LED
import time
# There is only one builtin LED on the BlackPill.
BUILTIN_LED_NUM = 1
# A button connected to pin PB10
USER_BUTTON_PIN = 'PB10'

# Builtin LED
led = LED(BUILTIN_LED_NUM)

#user button pulled up to VCC with a resistor
user = Pin(USER_BUTTON_PIN, Pin.IN, Pin.PULL_UP)

try:
    print("----------------")
    print("Program started.")
    print("* Using Builtin LED at {}.".format(led))
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
