#!/usr/bin/env python3

import time
from rpi_ws281x import *
import argparse
from rpi_ws281x import Color
from rpi_ws281x import Adafruit_NeoPixel

# LED strip configuration:
LED_COUNT      = 300     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating a signal (try 10)
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45, or 53

# Changeable
LED_BRIGHTNESS = 50     # Set to 0 for darkest and 255 for brightest

def setTreeColors(strip):
    # Set the top third of the tree to orange (darker shade)
    for i in range(2 * strip.numPixels() // 3, strip.numPixels()):
        strip.setPixelColor(i, Color(255,69,0))

    # Set the middle third of the tree to white
    for i in range(strip.numPixels() // 3, 2 * strip.numPixels() // 3):
        strip.setPixelColor(i, Color(255, 255, 255))

    # Set the bottom third of the tree to blue
    for i in range(strip.numPixels() // 3):
        strip.setPixelColor(i, Color(0, 0, 255))

    strip.show()

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
            # Set the colors of the tree
            setTreeColors(strip)

            # Continue to loop indefinitely
            pass

    except KeyboardInterrupt:
        if args.clear:
            # Clear the LEDs on exit
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, Color(0, 0, 0))
            strip.show()
