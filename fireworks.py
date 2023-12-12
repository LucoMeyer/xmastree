#!/usr/bin/env python3

import time
import math
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

def makeFirework(strip, color, peak, spread, wait_ms=50):
    """Simulate a firework with a peak and spread."""
    for i in range(peak - spread, peak + spread):
        if 0 <= i < strip.numPixels():
            strip.setPixelColor(i, color)
    strip.show()
    time.sleep(wait_ms/1000.0)

    # Fade out
    for i in range(255, 0, -10):
        for j in range(peak - spread, peak + spread):
            if 0 <= j < strip.numPixels():
                r, g, b = color >> 16, (color >> 8) & 0xFF, color & 0xFF
                strip.setPixelColor(j, Color(max(r-i,0), max(g-i,0), max(b-i,0)))
        strip.show()
        time.sleep(wait_ms/1000.0)

try:
    while True:
        # Clear strip
        colorWipe(strip, Color(0,0,0), 10)
        
        # Create a firework effect
        makeFirework(strip, Color(255, 0, 0), 150, 30, 100) # Red firework
        makeFirework(strip, Color(0, 255, 0), 75, 30, 100)  # Green firework
        makeFirework(strip, Color(0, 0, 255), 225, 30, 100) # Blue firework

except KeyboardInterrupt:
    colorWipe(strip, Color(0,0,0), 10)

