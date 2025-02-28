class TaskStore:
    def __init__(self):
        self.tasks = []
        self.task_id_counter = 1

    def get_all(self):
        return self.tasks

    def get_by_id(self, task_id):
        return next((task for task in self.tasks if task['id'] == task_id), None)

    def create(self, title, description=''):
        task = {
            'id': self.task_id_counter,
            'title': title,
            'description': description,
            'completed': False
        }
        self.tasks.append(task)
        self.task_id_counter += 1
        return task

    def update(self, task_id, data):
        task = self.get_by_id(task_id)
        if task:
            task['title'] = data.get('title', task['title'])
            task['description'] = data.get('description', task['description'])
            task['completed'] = data.get('completed', task['completed'])
        return task

    def delete(self, task_id):
        task = self.get_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False 