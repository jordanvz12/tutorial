import unittest
from Calculator.Calculator import Calculator
from Calculator.Calculator import ChildCalculator

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
        self.calculator = ChildCalculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_calculator_return_sum(self):
        result = self.calculator.Sum(1,2)
        self.assertEqual(3, result)

    def test_calculator_return_difference(self):
        result = self.calculator.Difference(1,2)
        self.assertEquals(-1, result)

    def test_childcalculator_return_sum(self):
        result = self.calculator.Sum(1,2)
        self.assertEqual(3, result)

    def test_childcalculator_return_difference(self):
        result = self.calculator.Difference(1,2)
        self.assertEquals(-1, result)

    def test_childcalculator_sum_list(self):
        valueList = [1,2,3]
        result = self.calculator.sumList(valueList)
        self.assertEqual(6, result)
