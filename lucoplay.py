#!/usr/bin/env python3

import time
from rpi_ws281x import *
from rpi_ws281x import Color
from rpi_ws281x import Adafruit_NeoPixel

import argparse
import random

# LED strip configuration:
LED_COUNT      = 300     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating a signal (try 10)
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45, or 53

# Changeable
LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
FIRE_PALETTE   = [Color(255, 69, 0), Color(255, 165, 0), Color(255, 255, 0)]

def fireEffect(strip):
    """Simulate a fire burning at the base of the tree."""
    flicker_rate = 0.2  # Adjust the flicker rate as needed

    for i in range(strip.numPixels()):
        flicker = random.uniform(0.5, 1.0)
        color = FIRE_PALETTE[random.randint(0, len(FIRE_PALETTE) - 1)]
        color = Color(int((color >> 16) & int(0xFF * flicker)), int((color >> 8) & int(0xFF * flicker)), int((color & 0xFF) * flicker))
        strip.setPixelColor(i, color)

    strip.show()
    time.sleep(flicker_rate)
    

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
            fireEffect(strip)

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0, 0, 0), 10)
