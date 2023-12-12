#!/usr/bin/env python3

import time
import os
import math
from rpi_ws281x import *
import argparse

# Added a comment

# LED strip configuration:
LED_COUNT      = 300     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ	   = 800000	 # LED signal frequency in hertz (usually 800khz)
LED_DMA		   = 10		 # DMA channel to use for generating a signal (try 10)
LED_INVERT	   = False	 # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL	   = 0		 # set to '1' for GPIOs 13, 19, 41, 45 or 53

#	Changeble
LED_BRIGHTNESS = 255	  # Set to 0 for darkest and 255 for brightest

def redSnake(strip, tail, offset):
	"""Send red snake across display."""
	for i in range(strip.numPixels() - offset, -1, -1):
		# print(f"Setting : {i}")
		if (i > tail+1):
			startColor = 215
			colorBandLimit = 40
			gap = math.ceil(colorBandLimit / tail)
			print(f"Gap : {gap}")
			for j in range(tail, -1, -1):
				colorBandLimit = colorBandLimit - gap
				if colorBandLimit < 0:
					colorBandLimit = 0
				print(f"Setting : {i-(j+1)} -> {colorBandLimit}")
				strip.setPixelColor(i-(j+1), Color(colorBandLimit, 0, 0))
		strip.setPixelColor(i, Color(255, 0, 0))
		# strip.setPixelColor(135, Color(0, 0, 0))

		strip.show()
		#time.sleep(wait_ms/1000.0)

def blueSnake(strip, tail, offset):
	"""Send bluered snake across display."""
	for i in range(strip.numPixels() - offset):
		# print(f"Setting : {i}")
		if (i > tail+1):
			startColor = 215
			colorBandLimit = 40
			gap = math.ceil(colorBandLimit / tail)
			print(f"Gap : {gap}")
			for j in range(tail):
				colorBandLimit = colorBandLimit - gap
				if colorBandLimit < 0:
					colorBandLimit = 0
				print(f"Setting : {i-(j+1)} -> {colorBandLimit}")
				strip.setPixelColor(i-(j+1), Color(0,0, colorBandLimit))
		strip.setPixelColor(i, Color(0, 0, 255))

		strip.show()
		#time.sleep(wait_ms/1000.0)

def greenSnake(strip, tail, offset):
	"""Send green snake across display."""
	for i in range(strip.numPixels() - offset):
		# print(f"Setting : {i}")
		if (i > tail+1):
			startColor = 215
			colorBandLimit = 40
			gap = math.ceil(colorBandLimit / tail)
			print(f"Gap : {gap}")
			for j in range(tail):
				colorBandLimit = colorBandLimit - gap
				if colorBandLimit < 0:
					colorBandLimit = 0
				print(f"Setting : {i-(j+1)} -> {colorBandLimit}")
				strip.setPixelColor(i-(j+1), Color(0, colorBandLimit, 0))
		strip.setPixelColor(i, Color(0, 255, 0))

		strip.show()
		#time.sleep(wait_ms/1000.0)

# Main program logic follows:
if __name__ == '__main__':
	# Process arguments
	parser = argparse.ArgumentParser()
	parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
	args = parser.parse_args()

	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')
	if not args.clear:
		print('Use "-c" argument to clear LEDs on exit')

	try:

		while True:
			redSnake(strip, 25, 0)
			blueSnake(strip, 25, 25)
			greenSnake(strip, 25, 50)
			redSnake(strip, 25, 75)
			blueSnake(strip, 25, 100)
			greenSnake(strip, 25, 120)

	except KeyboardInterrupt:
		if args.clear:
			colorWipe(strip, Color(0,0,0), 10)
