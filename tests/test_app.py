import unittest
from fastapi.testclient import TestClient

LOCAL_HOST = "http://localhost:8000"

from app.main import app

client = TestClient(app)


if __name__ == "__main__":
    unittest.main()
