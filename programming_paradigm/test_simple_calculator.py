# Objective: Learn the basics of unit testing in Python by writing tests for a provided SimpleCalculator class that supports addition, subtraction, multiplication, and division operations.

import unittest
from simple_calculator import SimpleCalculator

# Define a test case class that inherits from unittest.TestCase
# unitest.TestCase provides a framework for creating and running tests

class testSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        # This method is called before each test
        # It is used to set up any state that is shared across tests
        self.calc = SimpleCalculator()

    def test_addition(self):
        # Test the add method
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtraction(self):
        # Test the subtract method
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_multiplication(self):
        # Test the multiply method
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)

    def test_division(self):
        # Test the divide method
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero should return None