from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register():
    response = client.post('/register', json={'username': 'test', 'password': 'test'})
    assert response.status_code == 200
    assert response.json() == {'success': True}

def test_login():
    response = client.post('/login', json={'username': 'test', 'password': 'test'})
    assert response.status_code == 200
    assert response.json() == {'success': True}

def test_create_session():
    response = client.post('/session', json={'date': '2022-01-01', 'time': '10:00', 'place': 'Yoga Studio', 'max_participants': 10})
    assert response.status_code == 200
    assert response.json() == {'success': True}

def test_list_sessions():
    response = client.get('/sessions')
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_book_session():
    response = client.post('/book/0')
    assert response.status_code == 200
    assert response.json() == {'success': True}
