#!/usr/bin/env python3

import time
from rpi_ws281x import *
import argparse
from rpi_ws281x import Color
from rpi_ws281x import Adafruit_NeoPixel

def colorWipe(strip, color, wait_ms=10, start=0, end=None):
    """Wipe a solid color across display a pixel at a time."""
    if end is None:
        end = strip.numPixels() - 1

    for i in range(start, end + 1):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)

# LED strip configuration:
LED_COUNT      = 300     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating a signal (try 10)
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45, or 53

# Changeable
LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest

def runUp(strip, start, wait_ms=20):
    """Run a light up the LED strip."""
    for i in reversed(range(start, strip.numPixels())):
        strip.setPixelColor(i, Color(255, 255, 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)

def runDown(strip, start, wait_ms=20):
    """Run a light down the LED strip."""
    for i in range(start, strip.numPixels() - 1):  # Stop one position before the last LED
        strip.setPixelColor(i, Color(255, 255, 255))
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

    # Manually set the number of pixels
    num_pixels = strip.numPixels()

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:
        for i in reversed(range(strip.numPixels())):
            # Light up from bottom to top
            colorWipe(strip, Color(0, 0, int((i / num_pixels) * 255)), start=i)

            # Pause for a moment at the fully lit state
            time.sleep(0.5)  # Adjust the delay as needed

            # Turn off all LEDs except the last lit LED
            colorWipe(strip, Color(0, 0, 0), start=i, end=num_pixels)

        for i in range(strip.numPixels() - 1):
            # Light up from top to bottom, leaving one LED at the bottom unlit
            colorWipe(strip, Color(0, 0, int((i / num_pixels) * 255)), start=0, end=i + 1)

            # Pause for a moment at the fully lit state
            time.sleep(0.5)  # Adjust the delay as needed

            # Turn off all LEDs except the last lit LED
            colorWipe(strip, Color(0, 0, 0), start=0, end=i + 1)

        while True:
            # Continue to loop indefinitely, adding more LEDs if needed
            pass

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0, 0, 0))
