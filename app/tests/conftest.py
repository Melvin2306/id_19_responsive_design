from os import environ

environ['DATABASE_URL'] = 'sqlite://'


import pytest
from app.app import create_app

@pytest.fixture
def client():
    app = create_app()

    with app.app_context():
        yield app.test_client()