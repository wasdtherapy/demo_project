import unittest

from hello import greet


class TestGreet(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(greet("Аня"), "Привет, Аня!")

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            greet("")


if __name__ == "__main__":
    unittest.main()
