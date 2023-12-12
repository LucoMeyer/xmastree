#!/usr/bin/env python3

import time
import random
from rpi_ws281x import *

# LED strip configuration:
LED_COUNT      = 300
LED_PIN        = 18
LED_FREQ_HZ    = 800000
LED_DMA        = 10
LED_INVERT     = False
LED_CHANNEL    = 0
LED_BRIGHTNESS = 255

# Create NeoPixel object
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def twinkleStar(strip, wait_ms=200):
    """Randomly light up LEDs to simulate twinkling stars."""
    pixel = random.randint(0, strip.numPixels() - 1)
    brightness = random.randint(10, 255)
    color = Color(brightness, brightness, brightness) # White twinkle
    strip.setPixelColor(pixel, color)
    strip.show()
    time.sleep(wait_ms/1000.0)

try:
    while True:
        # Twinkle stars
        twinkleStar(strip)

        # Occasionally clear all LEDs to reset the twinkles
        if random.randint(0, 20) == 0:
            colorWipe(strip, Color(0,0,0), 10)

except KeyboardInterrupt:
    colorWipe(strip, Color(0,0,0), 10)

