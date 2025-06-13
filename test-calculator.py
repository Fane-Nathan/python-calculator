import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculator.addition(2, 3), 5)
        self.assertEqual(calculator.addition(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(calculator.subtraction(5, 3), 2)
        self.assertEqual(calculator.subtraction(3, 5), -2)

    def test_multiplication(self):
        self.assertEqual(calculator.multiplication(2, 3), 6)
        self.assertEqual(calculator.multiplication(-1, 5), -5)

    def test_division(self):
        self.assertEqual(calculator.division(6, 3), 2)
        self.assertEqual(calculator.division(5, 0), 'undefined (division by zero)')

    def test_modulus(self):
        self.assertEqual(calculator.modulus(5, 2), 1)
        self.assertEqual(calculator.modulus(5, 0), 'undefined (division by zero)')

    def test_exponentiation(self):
        self.assertEqual(calculator.exponentiation(2, 3), 8)
        self.assertEqual(calculator.exponentiation(5, 0), 1)

    def test_floor_division(self):
        self.assertEqual(calculator.floor_division(5, 2), 2)
        self.assertEqual(calculator.floor_division(5, 0), 'undefined (division by zero)')

if __name__ == '__main__':
    unittest.main()