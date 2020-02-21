from Operations.addition import Addition
from Operations.subtraction import Subtraction
from Operations.addLists import AddLists
class Calculator:
    Result = 0

    def __init__(self):
        pass

    def Sum(self, a, b):
        self.Result = Addition.sum(a,b)
        return self.Result

    def Difference(self, a, b):
        self.Result = Subtraction.difference(a,b)
        return self.Result

class ChildCalculator(Calculator):
    def sumList(self, valueList):
        self.Result = AddLists.sumLists(valueList)
        return self.Result