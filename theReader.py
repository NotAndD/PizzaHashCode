from PizzaMatrix import PizzaMatrix


class TheReader:

    def __init__(self, inputFileName):
        self.theMatrix = None
        self.fileName = inputFileName
        self.numberOfRows = 0
        self.numberOfColumns = 0
        self.minNumberOfIngredients = 0
        self.maxCellsInSlice = 0

    def readConfiguration(self):
        theFile = open(self.fileName)
        firstLine = theFile.readline().split(' ')
        self.numberOfRows = firstLine[0]
        self.numberOfColumns = firstLine[1]
        self.minNumberOfIngredients = firstLine[2]
        self.maxCellsInSlice = firstLine[3]
        lines = theFile.readlines()
        self.theMatrix = PizzaMatrix(lines)