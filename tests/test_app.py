import os
import unittest
import sys

module_location = os.environ["LOCATION"]
sys.path.insert(0, module_location)

from main import app


class TestApp(unittest.TestCase):
    ...


if __name__ == "__main__":
    unittest.main()
