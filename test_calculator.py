import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add(self):
            self.assertEqual(self.calc.add(-2, 2), 0)
    def test_add(self):
            self.assertEqual(self.calc.add(-2, -6), -8)

    def test_suntract(self):
            self.assertEqual(self.calc.subtract(257, 455), -198)
    def test_suntract(self):
            self.assertEqual(self.calc.subtract(849, 343), 506)
    def test_suntract(self):
                self.assertEqual(self.calc.subtract(-60, -9), -51)

    def test_multiply(self):
            self.assertEqual(self.calc.multiply(4, 2), 8)
    def test_multiply(self):
                self.assertEqual(self.calc.multiply(-5, 2), -10)
    def test_multiply(self):
                self.assertEqual(self.calc.multiply(-3, -2), 6)
    def test_multiply(self):
                self.assertEqual(self.calc.multiply(0, -2), 0)

    def test_divide(self):
                self.assertEqual(self.calc.divide(8, 2), 4)
    def test_divide(self):
                self.assertEqual(self.calc.divide(-6, 5), -1)
    def test_divide(self):
                self.assertEqual(self.calc.divide(240, 0), "หาค่าไม่ได้")

    def test_modulo(self):
                    self.assertEqual(self.calc.modulo(24, 8), 0)
    def test_modulo(self):
                    self.assertEqual(self.calc.modulo(69, 9), 6)
    def test_modulo(self):
                    self.assertEqual(self.calc.modulo(8, 24), 8)
    def test_modulo(self):
                    self.assertEqual(self.calc.modulo(240, 0), "หาค่าไม่ได้")
if __name__ == '__main__':
    unittest.main()
    