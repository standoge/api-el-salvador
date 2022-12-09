import unittest
import requests

LOCAL_HOST = "http://localhost:8000"


class TestApp(unittest.TestCase):
    """Unit test for endpoints"""

    def test_status(self):
        """Test to check if status code in root endpoint is OK."""
        response = requests.get(LOCAL_HOST)
        self.assertEqual(response.status_code, 200)

    def test_read_departament(self):
        """Test to check if departaments endpoint is responding."""
        response = requests.get(LOCAL_HOST + "/departaments/San Salvador")
        self.assertEqual(response.json()["depname"], "San Salvador")

    def test_read_municipality(self):
        """Test to check if municipalities endpoint is responding."""
        response = requests.get(LOCAL_HOST + "/townships/Colon")
        self.assertEqual(response.json()["munname"], "Colón")


if __name__ == "__main__":
    unittest.main()
