from flask import Blueprint, jsonify, request
from app.models.task_store import TaskStore

api = Blueprint('api', __name__)
task_store = TaskStore()

@api.route('/', methods=['GET'])
def welcome():
    return jsonify({'message': 'Welcome to the Task Manager API'})

@api.route('/api/v1/tasks', methods=['GET'])
def get_tasks():
    return jsonify(task_store.get_all())

@api.route('/api/v1/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    
    task = task_store.create(data['title'], data.get('description', ''))
    return jsonify(task), 201

@api.route('/api/v1/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = task_store.get_by_id(task_id)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(task)

@api.route('/api/v1/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = task_store.update(task_id, data)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(task)

@api.route('/api/v1/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_store.delete(task_id):
        return '', 204
    return jsonify({'error': 'Task not found'}), 404