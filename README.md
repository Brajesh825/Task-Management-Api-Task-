# Task Manager API

Welcome to the Task Manager API. This API allows you to manage tasks with basic CRUD operations.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [API Endpoints](#api-endpoints)
- [Error Handling](#error-handling)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone git@github.com:Brajesh825/Task-Management-Api-Task-.git
    ```
2. Navigate to the project directory:
    ```sh
    cd task-manager-api
    ```
3. Create a virtual environment:
    ```sh
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```
5. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

6. Install pytest:
    ```sh
    pip install pytest
    ```

## Usage

1. Run the Flask application:
    ```sh
    flask run
    ```
2. The API will be available at `http://localhost:5000`.

## Running Tests

To run the tests, use the following command:
```sh
python -m pytest
```

## API Endpoints

- `GET /` - Welcome message
- `GET /api/v1/tasks` - Retrieve all tasks
- `POST /api/v1/tasks` - Create a new task
- `GET /api/v1/tasks/<int:task_id>` - Retrieve a specific task by ID
- `PUT /api/v1/tasks/<int:task_id>` - Update a specific task by ID
- `DELETE /api/v1/tasks/<int:task_id>` - Delete a specific task by ID

## Error Handling

- `404 Not Found` - Returned when a requested resource is not found.
- `400 Bad Request` - Returned when the request is invalid or missing required parameters.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.