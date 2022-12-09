import unittest
import requests

LOCAL_HOST = "http://localhost:8000"


class TestApp(unittest.TestCase):
    """Unit test for endpoints"""

    def test_status(self):
        response = requests.get(LOCAL_HOST)
        self.assertEqual(response.status_code, 200)

    def test_read_departament(self):
        response = requests.get(LOCAL_HOST+"/departaments/San Salvador")
        self.assertEqual(response.json().depname,"San Salvador" )


if __name__ == "__main__":
    unittest.main()
