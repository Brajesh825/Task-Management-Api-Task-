import pytest
import json
from app import create_app

@pytest.fixture
def client():
    app = create_app('testing')
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_get_all_tasks(client):
    response = client.get('/api/v1/tasks')
    print(response.json)  # Log the response
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_create_task(client):
    response = client.post('/api/v1/tasks', data=json.dumps({
        'title': 'New Task',
        'description': 'New Task Description'
    }), content_type='application/json')
    print(response.json)  # Log the response
    assert response.status_code == 201
    assert response.json['title'] == 'New Task'
    assert response.json['description'] == 'New Task Description'


def test_delete_task(client):
    client.post('/api/v1/tasks', data=json.dumps({
        'title': 'New Task'
    }), content_type='application/json')
    response = client.delete('/api/v1/tasks/1')
    print(response.status_code)  # Log the response status code
    assert response.status_code == 204
    response = client.get('/api/v1/tasks/1')
    print(response.status_code)  # Log the response status code
    assert response.status_code == 404
