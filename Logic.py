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
            currSlice = Slice(x,y)
            self.slices.append(currSlice)
            self.exploreForMinimum(currSlice)

    def exploreForMinimum(self, slice):
        counter = {'M' : 0, 'T' : 0}




    def getStartingPositions(self, pizzaMatrix, minIngredient):
        startingPositions = []
        for i in range(pizzaMatrix):
            for j in range(pizzaMatrix):
                if not pizzaMatrix[i][j].explored and pizzaMatrix[i][j].type == minIngredient:
                    startingPositions.append((i,j))
        return startingPositions




