import unittest
from app.models.task_store import TaskStore

class TestTaskStore(unittest.TestCase):

    def setUp(self):
        self.store = TaskStore()

    def test_create_task(self):
        task = self.store.create('Test Task', 'Test Description')
        self.assertEqual(task['title'], 'Test Task')
        self.assertEqual(task['description'], 'Test Description')
        self.assertFalse(task['completed'])
        self.assertEqual(task['id'], 1)

    def test_get_all_tasks(self):
        self.store.create('Test Task 1')
        self.store.create('Test Task 2')
        tasks = self.store.get_all()
        self.assertEqual(len(tasks), 2)

    def test_get_task_by_id(self):
        task = self.store.create('Test Task')
        fetched_task = self.store.get_by_id(task['id'])
        self.assertEqual(fetched_task, task)

    def test_update_task(self):
        task = self.store.create('Test Task')
        updated_task = self.store.update(task['id'], {'title': 'Updated Task', 'completed': True})
        self.assertEqual(updated_task['title'], 'Updated Task')
        self.assertTrue(updated_task['completed'])

    def test_delete_task(self):
        task = self.store.create('Test Task')
        result = self.store.delete(task['id'])
        self.assertTrue(result)
        self.assertIsNone(self.store.get_by_id(task['id']))

    def test_delete_nonexistent_task(self):
        result = self.store.delete(999)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
