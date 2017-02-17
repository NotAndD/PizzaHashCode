from functools import reduce

from theReader import TheReader


class Brain:
    def __init__(self, configFile):
        self.reader = TheReader(configFile)
        self.reader.readConfiguration()

    def searchMinOccurencesOfIngredient(self):
        numResult = reduce(lambda a,b : a+b, map(lambda pizzaRow : map(lambda cell:1 if(cell.type == 'M') else -1), self.reader.theMatrix.matrix))
        return 'M' if numResult > 0 else 'T'