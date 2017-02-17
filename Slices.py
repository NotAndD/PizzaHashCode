
class Slice:
    def __init__(self, theMatrix, x1, y1):
        self.theMatrix = theMatrix
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1
        self.y2 = y1
        self.numOfCells = 1

    def addCells(self, x, y):
        if not self.checkPosition(x, y):
            raise Exception("collision on adding")
        if self.x1 > x:
            self.x1 = x
        if self.x2 < x:
            self.x2 = x
        if self.y1 > y:
            self.y1 = y
        if self.y2 < y:
            self.y2 = y

    def countIngredient(self, ingredient):
        counter = 0
        for i in range(self.x1, self.x2 + 1):
            for j in range(self.y1, self.y2 + 1):
                if self.theMatrix[i][j] == ingredient:
                    counter += 1
        return counter

    def checkInterception(self, otherSlice):
        theResult = False
        for i in range(self.x1, self.x2 + 1):
            for j in range(self.y1, self.y2 + 1):
                theResult = theResult or self.checkPosition(i, j)
        return theResult

    def checkPosition(self, x, y):
        if (self.x1 < x < self.x2 or self.x2 < x < self.x1) and (self.y1 < y < self.y1 or self.y2 < y < self.y1):
            return False
        return True