import unittest
from unittest import TestCase
from calculator import Calculator


class CalculatorTest(TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, 5), 0)
        self.assertAlmostEqual(self.calc.add(0.765, -4.523), -3.758)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertAlmostEqual(self.calc.subtract(0.765, 4.523), -3.758)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(2, 2), 4)
        self.assertAlmostEqual(self.calc.multiply(0.765, 4.523), 3.460095)

    def test_divide(self):
        self.assertEqual(self.calc.divide(0, 2), 0)
        self.assertAlmostEqual(self.calc.divide(4.523, 0.765), 5.912418300653595)
        self.assertRaises(ZeroDivisionError, lambda: self.calc.divide(1, 0))

    def test_evaluate(self):
        self.assertEqual(self.calc.evaluate('1+2'), 3)
        self.assertAlmostEqual(self.calc.evaluate('4*8/4'), 8.0)
        self.assertAlmostEqual(self.calc.evaluate('24-8*3+3*6/2'), 9.0)
        self.assertRaises(SyntaxError, lambda: self.calc.evaluate('23-67*'))

if __name__ == '__main__':
    unittest.main()