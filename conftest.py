import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture(scope="session")
def app_client():
    with TestClient(app=app) as client:
        yield client
