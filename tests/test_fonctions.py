import unittest
from maths.functions_maths import sum, multiplication

class TestFonctions(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(1, 2), 3)
        self.assertEqual(sum(-1, 1), 0)

    def test_multiplication(self):
        self.assertEqual(multiplication(2, 3), 6)
        self.assertEqual(multiplication(0, 3), 0)


if __name__ == '__main__':
    unittest.main()
