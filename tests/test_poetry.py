import unittest
from poetry import generate_random_poem, display_poem
from io import StringIO
import sys

class TestPoetry(unittest.TestCase):

    def test_generate_random_poem_returns_string(self):
        poem = generate_random_poem()
        self.assertIsInstance(poem, str)

    def test_generate_random_poem_returns_poem_with_6_lines(self):
        poem = generate_random_poem()
        self.assertEqual(len(poem.split('\n')), 6)

    def test_display_poem_prints_poem(self):
        poem = generate_random_poem()
        captured_output = StringIO()
        sys.stdout = captured_output
        display_poem(poem)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), poem)

if __name__ == '__main__':
    unittest.main()
