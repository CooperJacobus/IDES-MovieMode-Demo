        import random
        manualMode = True # exposure mode: true for manual, false for random
        fade = False # phosphorus fade: reduces grid values over time if true
        go = False # toggels exposures, controled by ENTER

        dimension = 4 # dimension of grid
        maxExposure = 256 # maximum exposures
        totalExposure = 0 # counter for exposures
        int[][] grid = new int[dimension][dimension] # 2D array of int values representing total exposure of each panel
        rowIndex = 0 # row index of currently exposed panel
        colIndex = 0 # column index of currently exposed panel
        eTime = 0 # countdown of remaining exposure;
        exposureTime = 0 # represenents how long panel is to be exposed for

# Manual Mode
        if manualMode:
            if go == False:
                # control variables with keys

            if go:
                # expose panel
                if fade:
                    grid[rowIndex][colIndex]+=5 # increase values for legibility if fade is on
                else:
                    grid[rowIndex][colIndex] += 1 # add to grid value
                    totalExposure += 1 # add to counter
                    eTime += 1 # subtract from remaining exposure time
                    # wait 50 milliseconds for legibility

                    # draw step in Piano Roll

            # stop run when time expires
            if eTime <= 0:
                go = False
                # wait 100 miliseconds

        # Random Mode
        if manualMode == False && go == True:
            if totalExposure < maxExposure:
                if eTime <= 0:
                    # randomly generate panel index and exposure time
                    rowIndex = int (random.random() * dimension)
                    colIndex = int (random.random() * dimension)
                    eTime = int (random.random() * 6) + 2
                    exposureTime = eTime
                else:
                    if fade:
                        grid[rowIndex][colIndex] += 5 # adjust for fade for legibility
                    else:
                        grid[rowIndex][colIndex] += 1 # add to grid value
                        totalExposure += 1 # add to counter
                        eTime -= 1 # subtract from remaining exposure time
                    # wait 50 miliseconds




        # reduce values in grid over time
        if fade:
            for x in xrange(dimension):
                for y in xrange(dimension):
                    if grid[x][y] > 0:
                        grid[x][y] -= 1




