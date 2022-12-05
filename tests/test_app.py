import unittest
import sys

sys.path.insert(0, "/home/doge/development/Python/api/app")

from main import app


class TestApp(unittest.TestCase):
    ...


if __name__ == "__main__":
    unittest.main()
