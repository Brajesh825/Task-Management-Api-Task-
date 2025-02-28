import unittest
import json
from app import create_app

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_get_all_tasks(self):
        response = self.client.get('/api/v1/tasks')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_create_task(self):
        response = self.client.post('/api/v1/tasks', data=json.dumps({
            'title': 'New Task',
            'description': 'New Task Description'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['title'], 'New Task')
        self.assertEqual(response.json['description'], 'New Task Description')

    def test_get_single_task(self):
        self.client.post('/api/v1/tasks', data=json.dumps({
            'title': 'New Task'
        }), content_type='application/json')
        response = self.client.get('/api/v1/tasks/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['title'], 'New Task')

    def test_update_task(self):
        self.client.post('/api/v1/tasks', data=json.dumps({
            'title': 'New Task'
        }), content_type='application/json')
        response = self.client.put('/api/v1/tasks/1', data=json.dumps({
            'title': 'Updated Task',
            'completed': True
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['title'], 'Updated Task')
        self.assertTrue(response.json['completed'])

    def test_delete_task(self):
        self.client.post('/api/v1/tasks', data=json.dumps({
            'title': 'New Task'
        }), content_type='application/json')
        response = self.client.delete('/api/v1/tasks/1')
        self.assertEqual(response.status_code, 204)
        response = self.client.get('/api/v1/tasks/1')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
