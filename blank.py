#!/usr/bin/env python3

import time
import os
import math
from rpi_ws281x import *
import argparse


# LED strip configuration:
LED_COUNT      = 300     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ	   = 800000	 # LED signal frequency in hertz (usually 800khz)
LED_DMA		   = 10		 # DMA channel to use for generating a signal (try 10)
LED_INVERT	   = False	 # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL	   = 0		 # set to '1' for GPIOs 13, 19, 41, 45 or 53

#	Changeble
LED_BRIGHTNESS = 255	  # Set to 0 for darkest and 255 for brightest

strip.setPixelColor(i, Color(255, 0, 0))
strip.show()
