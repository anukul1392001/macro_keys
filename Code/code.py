# Name - Anukul Anand
# Date - 23/06/2021
# Time - 3:22 PM
# Community - PointBlank <./>  https://pointblank.club/
# git_hub - https://github.com/anukul1392001/


# The Raspberry Pi Pico (RP2040) uses "CircuitPython" Firmware


import board
import time
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

#Toggle Key attached to GPIO Pin15 on Rpi Pico
key_pin = board.GP15

#It can be used to emulate a peripheral such as a mouse or keyboard via 'usb_hid' module
key_board = Keyboard(usb_hid.devices)

#Declare GPIO pin 15 as Digital IO
key1 = digitalio.DigitalInOut(key_pin)

#Declare GPIO pin 15 as INPUT
key1.direction = digitalio.Direction.INPUT

#Pull down the GPIO Pin 15 also Pull up can be used
key1.pull = digitalio.Pull.DOWN


while True:
    if key1.value:                                   #Use  'if !key.value'  in case of Pull up as pressing the switch will give 0 logic at the Pin 15
        print("key_pressed")
        key_board.press(Keycode.ALT, Keycode.TAB)    #keys which are to be emulated, for more refer https://circuitpython.readthedocs.io/projects/hid/en/latest/api.html#
        time.sleep(0.6)                              #delay 0.6 seconds
        key_board.release(Keycode.ALT, Keycode.TAB)  #release the keys after 0.6 seconds