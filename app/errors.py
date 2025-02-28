from flask import Blueprint, jsonify, render_template, request

errors = Blueprint('errors', __name__)

def is_api_request():
    return request.path.startswith('/api/')

@errors.app_errorhandler(404)
def not_found_error(error):
    if is_api_request():
        return jsonify({'error': 'Resource not found'}), 404
    return render_template('errors/404.html'), 404

@errors.app_errorhandler(500)
def internal_error(error):
    if is_api_request():
        return jsonify({'error': 'Internal server error'}), 500
    return render_template('errors/500.html'), 500

@errors.app_errorhandler(400)
def bad_request_error(error):
    if is_api_request():
        return jsonify({'error': 'Bad request'}), 400
    return render_template('errors/400.html'), 400 