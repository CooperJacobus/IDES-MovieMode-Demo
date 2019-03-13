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
options.pixel_mapper_config = 'U-mapper;Rotate:90'

manualMode = False  # exposure mode: true for manual, false for random
fade = True  # phosphorus fade: reduces grid values over time if true
go = False  # toggels exposures, controlled by ENTER

dimension = 4
maxExposure = 256  # maximum exposures
totalExposure = 0  # counter for exposures
grid = [[0 for x in range(dimension)] for y in range(dimension)]  # 2D array of int values representing total exposure of each panel
rowIndex = 0  # row index of currently exposed panel
colIndex = 0  # column index of currently exposed panel
eTime = 0  # countdown of remaining exposure;

matrix = RGBMatrix(options=options)

if manualMode == False:
    while totalExposure < maxExposure*dimension | fade:
        if eTime <= 0:
            # randomly generate panel index and exposure time
            rowIndex = int(random.random() * dimension)
            colIndex = int(random.random() * dimension)
            while grid[rowIndex][colIndex] >= 25:  # ensure no panel is overexposed
                rowIndex = int(random.random() * dimension)
                colIndex = int(random.random() * dimension)
            eTime = int(random.random() * 6) + 2
        else:
            if fade:
                grid[rowIndex][colIndex] += 4  # amplify if fade is on
            grid[rowIndex][colIndex] += 1  # add to grid value
            totalExposure += 1  # add to counter
            eTime -= 1  # subtract from remaining exposure time

            if grid[rowIndex][colIndex] >= 25:
                grid[rowIndex][colIndex] = 25  # set upper bound

        if fade:
            for row in range(dimension):
                for col in range(dimension):
                    if grid[row][col] > 0:
                        grid[row][col] -= 1

        for row in range(0, dimension):
            for col in range(0, dimension):
                for x in range(0, matrix.width/dimension):
                    for y in range(0, matrix.height/dimension):
                        if fade:
                            matrix.SetPixel((matrix.width/dimension) * row + x, (matrix.height/dimension) * col + y, 0, grid[row][col] * 10, grid[row][col] * 2)
                        else:
                            matrix.SetPixel((matrix.width / dimension) * row + x, (matrix.height / dimension) * col + y, 0, grid[row][col] * 10, grid[row][col] * 2)

        if not fade & totalExposure >= maxExposure*dimension/2:
            for row in range(0,dimension):
                for col in range(0,dimension):
                    grid[row][col] = 0  # reset each grid value once sequence is complete
        time.sleep(0.050)

try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)

