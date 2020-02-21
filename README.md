# H1 tutorial
This is a quick and simple tutorial on the essential Object Oriented Programming Concepts with code and explanation. 
## H2 Encapsulation
In this program there is an addition method and a subtraction method that are called in the Calculator class. The test_calculator.py file creates an instance of the Calculator class by creating a Calculator object and adds data to those object and passes the method to verify the result.

    'def Sum(self, a, b):
        self.Result = Addition.sum(a,b)
        return self.Result
    def Difference(self, a, b):
        self.Result = Subtraction.difference(a,b)
        return self.Result'
        
        
## H2 Abstraction
The attributes and properties of a class are the abstract characteristics of the class. In this case the class Calculator contains abstract characteristics like the methods subtraction and addition. 

## H2 Inheritance
In this program the Calculator class is a parent class to the ChildCalculator class. The ChildCalculator class inherits all the methods of the Calculator class and can perform the same functions using the addition and subtraction methods.

'class ChildCalculator(Calculator):'


## H2 Polymorphism
> blockquote The child class, ChildCalculator inherits everything from its parent Calculator class. The child however, does not have to inherit everything from the parent, that is, the child can do some things differently. Unlike the parent, the child class can sum up lists. 
'class ChildCalculator(Calculator):
    def sumList(self, valueList):
        self.Result = AddLists.sumLists(valueList)
        return self.Result'
