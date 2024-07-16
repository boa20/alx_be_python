# Import the unittest module

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(3, -2), 1)
        # Add more assertions to thoroughly test the add method.

    def test_subtraction(self):
        """Test the addition method."""
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(2, -1), 3)
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiplication(self):
        """Test the addition method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(1, -1), -1)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(2, 0), 0)
        self.assertEqual(self.calc.multiply(0, 4), 0)

    def test_divide(self):
        """Test the addition method."""
        self.assertEqual(self.calc.divide(2, 4), 0.5)
        self.assertEqual(self.calc.divide(-1, 1), -1)
        self.assertEqual(self.calc.divide(1, -1), -1)
        self.assertEqual(self.calc.divide(-5, -5), 1)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(2, 0), ZeroDivisionError)
        #self.assertRaises(ZeroDivisionError, self.calc.divide(2, 0))

# Remember to write additional test methods for subtract, multiply, and divide.