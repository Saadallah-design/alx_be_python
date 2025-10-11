# Objective: Learn the basics of unit testing in Python by writing tests for a provided SimpleCalculator class that supports addition, subtraction, multiplication, and division operations.

import unittest
from simple_calculator import SimpleCalculator

# Define a test case class that inherits from unittest.TestCase
# unitest.TestCase provides a framework for creating and running tests

class testSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        # This method is called before each test
        # It is used to set up any state that is shared across tests
        self.calculator = SimpleCalculator()

    def test_add(self):
        # Test the add method
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(-1, -1), -2)

    def test_subtract(self):
        # Test the subtract method
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(0, 0), 0)
        self.assertEqual(self.calculator.subtract(-1, -1), 0)

    def test_multiply(self):
        # Test the multiply method
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-1, 1), -1)
        self.assertEqual(self.calculator.multiply(-1, -1), 1)

    def test_divide(self):
        # Test the divide method
        self.assertEqual(self.calculator.divide(6, 3), 2)
        self.assertEqual(self.calculator.divide(-6, 3), -2)
        self.assertIsNone(self.calculator.divide(5, 0))  # Division by zero should return None