import unittest
from app.main import add

class TestMain(unittest.TestCase):
    def test_add(self):
        """
        Test case for the add function
        """
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

if __name__ == "__main__":
    unittest.main()