# Objective: Learn the basics of unit testing in Python by writing tests for a provided SimpleCalculator class that supports addition,
#  subtraction, multiplication, and division operations.
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(self, 5, 3), 8)
        self.assertEqual(self.calc.add(self, -2, 2), 0)
        self.assertEqual(self.calc.add(self, 0, 0), 0)
        self.assertEqual(self.calc.add(self, 10, -5), 5)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(self, 5, 3), 2)
        self.assertEqual(self.calc.subtract(self, -2, 2), -4)
        self.assertEqual(self.calc.subtract(self, 0, 0), 0)
        self.assertEqual(self.calc.subtract(self, 10, -5), 15)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(self, 5, 3), 15)
        self.assertEqual(self.calc.multiply(self, -2, 2), -4)
        self.assertEqual(self.calc.multiply(self, 0, 5), 0)
        self.assertEqual(self.calc.multiply(self, 10, -5), -50)
    def test_division(self):
        self.assertEqual(self.calc.divide(self, 5, 2), 2.5)
        self.assertEqual(self.calc.divide(self, 5, 0), None)
        self.assertEqual(self.calc.divide(self, 0, 5), 0)
        self.assertEqual(self.calc.divide(self, -10, 2), -5)

if __name__ == '__main__':
    unittest.main()
