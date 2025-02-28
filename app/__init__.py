from flask import Flask, jsonify
from app.routes.api import api as api_blueprint
from config import config

def create_app(config_name='default'):
    app = Flask(__name__)
    
    # Load config
    app.config.from_object(config[config_name])
    
    # Register blueprints
    app.register_blueprint(api_blueprint)
    
    # Catch-all route for undefined routes
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Page not found'}), 404
    
    return app