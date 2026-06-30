import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test that the home route returns a 200 OK and correct JSON."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'

def test_multiply_route(client):
    """Test that our math logic works via the API."""
    response = client.get('/multiply/5/4')
    assert response.status_code == 200
    assert response.json['result'] == 200  # <--- intentional bug for you to watch fail first!
