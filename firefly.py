#!/usr/bin/env python3

import time
import random
from rpi_ws281x import *
import argparse
from rpi_ws281x import Adafruit_NeoPixel
from rpi_ws281x import Color


#!/usr/bin/env python3

#!/usr/bin/env python3

import time
import os
import math
from rpi_ws281x import *
import argparse
import random

# LED strip configuration:
LED_COUNT      = 300     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating a signal (try 10)
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Changeable
LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest

def fireflyEffect(strip):
    """Simulate white fireflies with blue tails."""
    for i in range(strip.numPixels()):
        # Dim existing pixels
        color = strip.getPixelColor(i)
        r = (color >> 16) & 0xFF
        g = (color >> 8) & 0xFF
        b = color & 0xFF
        r = max(0, r - 5)  # Dim red component
        g = max(0, g - 5)  # Dim green component
        b = max(0, b - 5)  # Dim blue component
        strip.setPixelColor(i, Color(r, g, b))

    # Add new firefly with blue tail
    index = random.randint(0, strip.numPixels() - 1)
    strip.setPixelColor(index, Color(0, 0, 255))  # Blue tail
    strip.setPixelColor(index + 1, Color(255, 255, 255))  # White firefly
    strip.show()
    time.sleep(0.05)


def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Initialize the library (must be called once before other functions).
    strip.begin()

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:
        while True:
            fireflyEffect(strip)

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0, 0, 0), 10)
