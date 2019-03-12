import random
import time


class Demo():
    def __init__(self, *args, **kwargs):
        super(Demo, self).__init__(*args, **kwargs)

        def run(self):
            while True:
                offset_canvas = self.matrix.CreateFrameCanvas()

                manualMode = False  # exposure mode: true for manual, false for random
                fade = False  # phosphorus fade: reduces grid values over time if true
                go = True  # toggels exposures, controlled by ENTER

                dimension = 4  # type: int # dimension of grid
                maxExposure = 256  # maximum exposures
                totalExposure = 0  # counter for exposures
                grid = [[0 for x in range(dimension)] for y in
                        range(dimension)]  # 2D array of int values representing total exposure of each panel
                rowIndex = 0  # row index of currently exposed panel
                colIndex = 0  # column index of currently exposed panel
                eTime = 0  # countdown of remaining exposure;
                exposureTime = 0  # represenents how long panel is to be exposed for

                for row in range(dimension):
                    for col in range(dimension):
                        for x in range(self.matrix.width/dimension):
                            for y in range(self.matrix.height / dimension):
                                offset_canvas.SetPixel(row * (self.matrix.width / dimension) + x, col * (self.matrix.height / dimension) + y, 0, grid[row][col]*10, grid[row][col]*6)

                # Manual Mode

                # Random Mode
                if manualMode == False & go == True:
                    if totalExposure < maxExposure:
                        if eTime <= 0:
                            # randomly generate panel index and exposure time
                            rowIndex = int(random.random() * dimension)
                            colIndex = int(random.random() * dimension)
                            eTime = int(random.random() * 6) + 2
                            exposureTime = eTime
                        else:
                            if fade:
                                grid[rowIndex][colIndex] += 5  # adjust for fade for legibility
                            else:
                                grid[rowIndex][colIndex] += 1 # add to grid value
                                totalExposure += 1 # add to counter
                                eTime -= 1  # subtract from remaining exposure time
                                time.sleep(0.005)  # wait 50 milliseconds

                # reduce values in grid over time
                if fade:
                    for x in xrange(dimension):
                        for y in xrange(dimension):
                            if grid[x][y] > 0:
                                grid[x][y] -= 1

