from fastapi.testclient import TestClient
from fastapi import status
from app.main import app

client = TestClient(app=app)

def test_index_returns_connect():
    response = client.get('/api/healthchecker')
    
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Welcome to API Mutosi"}

    

