# Task Manager API

A Flask-based REST API for managing tasks with both API endpoints and web interface.

## Features

- RESTful API endpoints
- Web interface for task management
- Error handling and logging
- CSRF protection
- Environment-specific configurations
- JSON structured logging

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd task-manager
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set environment variables (optional):
```bash
# Windows
set FLASK_ENV=development
set SECRET_KEY=your-secret-key

# Linux/MacOS
export FLASK_ENV=development
export SECRET_KEY=your-secret-key
```

5. Run the application:
```bash
python run.py
```

The application will be available at `http://localhost:5000`

## API Documentation

### Task Endpoints

#### Get All Tasks
- **URL**: `/api/v1/tasks`
- **Method**: `GET`
- **Success Response**:
  - **Code**: 200
  - **Content**:
    ```json
    [
      {
        "id": 1,
        "title": "Task 1",
        "description": "Description 1",
        "completed": false
      }
    ]
    ```

#### Create Task
- **URL**: `/api/v1/tasks`
- **Method**: `POST`
- **Data Params**:
  ```json
  {
    "title": "Task Title",
    "description": "Task Description" // optional
  }
  ```
- **Success Response**:
  - **Code**: 201
  - **Content**:
    ```json
    {
      "id": 1,
      "title": "Task Title",
      "description": "Task Description",
      "completed": false
    }
    ```
- **Error Response**:
  - **Code**: 400
  - **Content**: `{"error": "Title is required"}`

#### Get Single Task
- **URL**: `/api/v1/tasks/<task_id>`
- **Method**: `GET`
- **Success Response**:
  - **Code**: 200
  - **Content**:
    ```json
    {
      "id": 1,
      "title": "Task Title",
      "description": "Task Description",
      "completed": false
    }
    ```
- **Error Response**:
  - **Code**: 404
  - **Content**: `{"error": "Task not found"}`

#### Update Task
- **URL**: `/api/v1/tasks/<task_id>`
- **Method**: `PUT`
- **Data Params**:
  ```json
  {
    "title": "Updated Title",      // optional
    "description": "Updated Desc", // optional
    "completed": true             // optional
  }
  ```
- **Success Response**:
  - **Code**: 200
  - **Content**:
    ```json
    {
      "id": 1,
      "title": "Updated Title",
      "description": "Updated Desc",
      "completed": true
    }
    ```
- **Error Response**:
  - **Code**: 404
  - **Content**: `{"error": "Task not found"}`

#### Delete Task
- **URL**: `/api/v1/tasks/<task_id>`
- **Method**: `DELETE`
- **Success Response**:
  - **Code**: 204
- **Error Response**:
  - **Code**: 404
  - **Content**: `{"error": "Task not found"}`

## Web Interface

The application also provides a web interface accessible at:

- **Home**: `/` - List all tasks
- **New Task**: `/tasks/new` - Create a new task
- **Edit Task**: `/tasks/<task_id>/edit` - Edit an existing task

## Configuration

The application supports different environments:

- **Development**: Default configuration with debug mode
- **Production**: Optimized for production with security features
- **Testing**: Configuration for running tests

Set the environment using `FLASK_ENV`:
```bash
# Windows
set FLASK_ENV=production

# Linux/MacOS
export FLASK_ENV=production
```

## Security Features

- CSRF Protection
- Secure Session Configuration
- HTTP-only Cookies
- SameSite Cookie Policy
- Session Lifetime Limits

## Logging

Logs are stored in the `logs` directory:
- `task_manager.log`: All application logs
- `error.log`: Error-level logs only

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

### Get all tasks
- **GET** `/tasks`
- Returns a list of all tasks

### Create a task
- **POST** `/tasks`
- Request body:
```json
{
    "title": "Task title",
    "description": "Task description" (optional)
}
```

### Get a specific task
- **GET** `/tasks/<task_id>`
- Returns a single task by ID

### Update a task
- **PUT** `/tasks/<task_id>`
- Request body:
```json
{
    "title": "Updated title",
    "description": "Updated description",
    "completed": true
}
```
- All fields in the request body are optional

### Delete a task
- **DELETE** `/tasks/<task_id>`
- Deletes a task by ID

## Example Usage

Create a task:
```bash
curl -X POST http://localhost:5000/tasks \
    -H "Content-Type: application/json" \
    -d '{"title": "Learn Flask", "description": "Build a REST API"}'
```

Get all tasks:
```bash
curl http://localhost:5000/tasks
``` #   T a s k - M a n a g e m e n t - A p i - T a s k -  
 