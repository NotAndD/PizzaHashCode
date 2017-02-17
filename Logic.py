from functools import reduce

from Slices import Slice
from theReader import TheReader

class Brain:
    def __init__(self, configFile):
        self.reader = TheReader(configFile)
        self.reader.readConfiguration()
        self.slices = []

    def searchMinOccurencesOfIngredient(self):
        numResult = reduce(lambda a,b : a+b, map(lambda pizzaRow : map(lambda cell:1 if(cell.type == 'M') else -1), self.reader.theMatrix.matrix))
        return 'M' if numResult > 0 else 'T'

    def search(self):
        minIngredient = self.searchMinOccurencesOfIngredient()
        pizzaMatrix = self.reader.theMatrix.matrix
        while not self.reader.theMatrix.allExplored():
            startingPositions = self.getStartingPositions(pizzaMatrix, minIngredient)
            x,y = startingPositions[0]
            currSlice = Slice(self.reader.theMatrix.matrix, x, y)
            self.reader.theMatrix.matrix[x][y].explore()
            self.slices.append(currSlice)
            self.exploreForMinimum(currSlice, self.reader.theMatrix[x][y])

    def exploreForMinimum(self, slice, startingCell):
        counter = {'M' : 0, 'T' : 0}
        counter[startingCell.type] += 1
        while counter['M'] + counter['T'] < 2 * self.reader.minNumberOfIngredients:
            lenght = slice.lenght()
            height = slice.height()
            results = self.watchLeft(slice), self.watchTop(slice), self.watchRight(slice), self.watchDown(slice)
            maxRes = max(results)
            rightIndex = results.index(maxRes)


    def watchLeft(self, slice):
        points = 0
        numM, numT = slice.countIngredient('M'), slice.countIngredient('T')
        if slice.y1 > 0 :
            leftY = (slice.y1 - 1)
            for x in range(slice.x1, slice.x2 + 1):
                cell = self.reader.theMatrix.matrix[x][leftY]
                if cell.type == 'M' and numM < numT:
                    points += 10
                elif cell.type == 'M' and numM >= numT:
                    points += 5
                elif cell.type == 'T' and numT < numM:
                    points += 10
                else:
                    points += 5
        return points

    def watchRight(self, slice):
        points = 0
        numM, numT = slice.countIngredient('M'), slice.countIngredient('T')
        if slice.y2 < self.reader.numberOfRows :
            rightY = (slice.y2 + 1)
            for x in range(slice.x1, slice.x2 + 1):
                cell = self.reader.theMatrix.matrix[x][rightY]
                if cell.type == 'M' and numM < numT:
                    points += 10
                elif cell.type == 'M' and numM >= numT:
                    points += 5
                elif cell.type == 'T' and numT < numM:
                    points += 10
                else:
                    points += 5
        return points

    def watchDown(self, slice):
        points = 0
        numM, numT = slice.countIngredient('M'), slice.countIngredient('T')
        if slice.x2 < self.reader.numberOfRows:
            downX = (slice.x2 + 1)
            for y in range(slice.y1, slice.y2 + 1):
                cell = self.reader.theMatrix.matrix[downX][y]
                if cell.type == 'M' and numM < numT:
                    points += 10
                elif cell.type == 'M' and numM >= numT:
                    points += 5
                elif cell.type == 'T' and numT < numM:
                    points += 10
                else:
                    points += 5
        return points

    def watchTop(self, slice):
        points = 0
        numM, numT = slice.countIngredient('M'), slice.countIngredient('T')
        if slice.x1 > 0:
            topX = (slice.x1 - 1)
            for y in range(slice.y1, slice.y2 + 1):
                cell = self.reader.theMatrix.matrix[topX][y]
                if cell.type == 'M' and numM < numT:
                    points += 10
                elif cell.type == 'M' and numM >= numT:
                    points += 5
                elif cell.type == 'T' and numT < numM:
                    points += 10
                else:
                    points += 5
        return points

    def getStartingPositions(self, pizzaMatrix, minIngredient):
        startingPositions = []
        for i in range(pizzaMatrix):
            for j in range(pizzaMatrix):
                if not pizzaMatrix[i][j].explored and pizzaMatrix[i][j].type == minIngredient:
                    startingPositions.append((i,j))
        return startingPositions




