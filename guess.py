#!/usr/bin/env python3

import time
import random
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
LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest

# Christmas colors
CHRISTMAS_COLORS = [
    Color(0, 255, 0),    # Green
    Color(255, 0, 0),    # Red
    Color(0, 0, 255),    # Blue
    Color(0, 255, 255),  # Light Blue
    Color(144, 238, 144), # Light Green
    Color(255, 99, 71),   # Light Red
    Color(128, 0, 128),   # Purple
    Color(255, 182, 193), # Light Purple
    Color(255, 182, 193), # Light Pink
    Color(255, 223, 223), # Pink
    Color(255, 255, 0),   # Yellow
    Color(255, 165, 0),   # Orange
]

def fillTree(strip):
    """Fill up the entire tree with random Christmas colors, all LEDs staying on until completion."""
    illuminated_leds = set()

    while len(illuminated_leds) < strip.numPixels():
        # Choose a random LED that hasn't been illuminated yet
        led_index = random.randint(0, strip.numPixels() - 1)
        while led_index in illuminated_leds:
            led_index = random.randint(0, strip.numPixels() - 1)

        # Illuminate the chosen LED with a random Christmas color
        color = random.choice(CHRISTMAS_COLORS)
        strip.setPixelColor(led_index, color)
        strip.show()
        illuminated_leds.add(led_index)

        # Pause for a short duration
        time.sleep(0.1)

    # Pause for a moment at the fully lit state
    time.sleep(1)

    # Turn off all LEDs
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()

def main():
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Initialize the library (must be called once before other functions).
    strip.begin()

    print('Press Ctrl-C to quit.')

    try:
        while True:
            # Fill up the entire tree with random Christmas colors
            fillTree(strip)

    except KeyboardInterrupt:
        # Clear the LEDs on exit
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()

if __name__ == '__main__':
    main()
