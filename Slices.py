
class Slice:
    def __init__(self, theMatrix, x1, y1):
        self.theMatrix = theMatrix
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1
        self.y2 = y1
        self.numOfCells = 1

    def length(self):
        return self.y2 - self.y1 + 1

    def height(self):
        return self.x2 - self.x1 + 1

    def addCells(self, x, y):
        if not self.checkPosition(x, y):
            raise Exception("collision on adding")

        newx1 = self.x1
        newx2 = self.x2
        newy1 = self.y1
        newy2 = self.y2

        if self.x1 > x:
            newx1 = x
        if self.x2 < x:
            newx2 = x
        if self.y1 > y:
            newy1 = y
        if self.y2 < y:
            newy2 = y

        newSlice = Slice(self.theMatrix, newx1, newy1)
        newSlice.x2 = newx2
        newSlice.y2 = newy2
        newSlice.numOfCells = newSlice.length() * newSlice.height()

        return newSlice

    def countIngredient(self, ingredient):
        counter = 0
        for i in range(self.x1, self.x2 + 1):
            for j in range(self.y1, self.y2 + 1):
                if self.theMatrix[i][j] == ingredient:
                    counter += 1
        return counter

    def checkInterception(self, otherSlice):
        theResult = False
        for i in range(otherSlice.x1, otherSlice.x2 + 1):
            for j in range(otherSlice.y1, otherSlice.y2 + 1):
                theResult = theResult or self.checkPosition(i, j)
        return theResult

    def checkPosition(self, x, y):
        if (self.x1 < x < self.x2 or self.x2 < x < self.x1) and (self.y1 < y < self.y1 or self.y2 < y < self.y1):
            return False
        return True