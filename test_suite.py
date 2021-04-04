import unittest
import main

class TestMain(unittest.TestCase):

    # query validation tests
    # empty prompt
    def test_query(self):
        # empty prompt, returns false
        self.assertEqual(main.query(''), False)
        # whitespace prompt, returns false
        self.assertEqual(main.query(' '), False)
        self.assertEqual(main.query('    '), False)

if __name__ == "__main__":
    unittest.main()