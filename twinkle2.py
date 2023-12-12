#!/usr/bin/env python3

import time
import random
from rpi_ws281x import *
from rpi_ws281x import Color
from rpi_ws281x import Adafruit_NeoPixel

class RGB:
	def __init__(self, red, green, blue):
		self.red = red
		self.green = green
		self.blue = blue


# LED strip configuration:
LED_COUNT	   = 300
LED_PIN		   = 18
LED_FREQ_HZ	   = 800000
LED_DMA		   = 10
LED_INVERT	   = False
LED_CHANNEL	   = 0
LED_BRIGHTNESS = 49

stars = [None] * LED_COUNT

# Create NeoPixel object
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def twinkleStarOl(strip, wait_ms=200):
	"""Randomly light up LEDs to simulate twinkling stars."""
	pixel = random.randint(0, strip.numPixels() - 1)
	brightness = random.randint(10, 255)
	color = Color(brightness, brightness, brightness) # White twinkle
	strip.setPixelColor(pixel, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def twinkleStar(strip, wait_ms=200):
	"""Randomly light up LEDs to simulate twinkling stars."""
	pixel = random.randint(0, strip.numPixels() - 1)
	red = random.randint(10, 255)
	green = random.randint(10, 255)
	blue = random.randint(10, 255)

	rgb_color = RGB(red, green, blue)
	stars[pixel] = rgb_color

	# print(f"Setting light : {pixel}")
	color = Color(red, green, blue)
	strip.setPixelColor(pixel, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def fade(strip, wait_ms=200):
	chunk = 40
	for i in range(strip.numPixels()):
		if stars[i] is not None:
			rgb_color = stars[i]
			rgb_color.red = 0 if rgb_color.red <= chunk else rgb_color.red - chunk;
			rgb_color.green = 0 if rgb_color.green <= chunk else rgb_color.green - chunk;
			rgb_color.blue = 0 if rgb_color.blue <= chunk else rgb_color.blue - chunk;
			# print(f"Fading light : {i} to {rgb_color.red},{rgb_color.green},{rgb_color.blue}")
			stars[i] = rgb_color
			color = Color(int(rgb_color.red), int(rgb_color.green), int(rgb_color.blue))
			strip.setPixelColor(i, color)
	strip.show()
	#time.sleep(wait_ms/1000.0)


try:
	while True:
		# Twinkle stars
		burst = random.randint(0, 10)
		for i in range(burst):
			twinkleStar(strip, 0)

		time.sleep(200/1000.0)
		fade(strip, 0)

		# Occasionally clear all LEDs to reset the twinkles
		# if random.randint(0, 20) == 0:
			# colorWipe(strip, Color(0,0,0), 10)

except KeyboardInterrupt:
	colorWipe(strip, Color(0,0,0), 10)

