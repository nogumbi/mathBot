import unittest
from unittest.mock import patch
from io import StringIO
import app


class MyTestCase(unittest.TestCase):

    @patch("sys.stdin", StringIO("hello\nhi\nhi!"))
    def test_greeting(self):
        self.assertEqual(app, 'how do you do?')

if __name__ == '__main__':
    unittest.main()