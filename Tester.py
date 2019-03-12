#!/usr/bin/env python
import time
import sys
import random

from rgbmatrix import RGBMatrix, RGBMatrixOptions

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 2
options.parallel = 1
options.hardware_mapping = 'adafruit-hat-pwm'
dimension = 4

matrix = RGBMatrix(options = options)

for row in range(0, dimension):
    for col in range(0, dimension):
        shade = int(random.random()*255)
        for x in range(0,matrix.width/dimension):
            for y in range(0,matrix.height/dimension):
                matrix.SetPixel((matrix.width/dimension) * row + x, (matrix.height/dimension) * col + y, 0, shade, 0)
        time.sleep(0.025)
try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)

