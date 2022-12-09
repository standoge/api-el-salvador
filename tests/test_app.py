import unittest
import requests

LOCAL_HOST = "http://localhost:8000"


class TestApp(unittest.TestCase):
    """Unit test for endpoints"""

    def test_status(self):
        response = requests.get(LOCAL_HOST)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
