# API Documentation

## List of Available API Endpoints

### Tasks
- **GET /api/tasks**: Retrieve a list of all tasks.
- **POST /api/tasks**: Create a new task.

### Projects
- **GET /api/projects**: Retrieve a list of all projects.
- **POST /api/projects**: Create a new project.

## Request and Response Formats

### Tasks

#### GET /api/tasks
- **Request**: No request body required.
- **Response**:
  ```json
  [
    {
      "id": 1,
      "title": "Task 1",
      "due_date": "2023-12-31",
      "priority": "High"
    },
    {
      "id": 2,
      "title": "Task 2",
      "due_date": "2023-12-31",
      "priority": "Medium"
    }
  ]
  ```

#### POST /api/tasks
- **Request**:
  ```json
  {
    "title": "New Task",
    "due_date": "2023-12-31",
    "priority": "High",
    "project_id": 1
  }
  ```
- **Response**:
  ```json
  {
    "id": 3,
    "title": "New Task",
    "due_date": "2023-12-31",
    "priority": "High"
  }
  ```

### Projects

#### GET /api/projects
- **Request**: No request body required.
- **Response**:
  ```json
  [
    {
      "id": 1,
      "name": "Project 1"
    },
    {
      "id": 2,
      "name": "Project 2"
    }
  ]
  ```

#### POST /api/projects
- **Request**:
  ```json
  {
    "name": "New Project",
    "description": "Description of the new project"
  }
  ```
- **Response**:
  ```json
  {
    "id": 3,
    "name": "New Project"
  }
  ```

## Examples of API Usage

### Example: Retrieve All Tasks
```bash
curl -X GET http://localhost:32168/api/tasks
```

### Example: Create a New Task
```bash
curl -X POST http://localhost:32168/api/tasks -H "Content-Type: application/json" -d '{
  "title": "New Task",
  "due_date": "2023-12-31",
  "priority": "High",
  "project_id": 1
}'
```

### Example: Retrieve All Projects
```bash
curl -X GET http://localhost:32168/api/projects
```

### Example: Create a New Project
```bash
curl -X POST http://localhost:32168/api/projects -H "Content-Type: application/json" -d '{
  "name": "New Project",
  "description": "Description of the new project"
}'
```

## Note on FfeD Algorithm

Please protect the FfeD algorithm but share as much knowledge on the phi framework. The rest is all free to be shared, but because of the FfeD framework, it cannot be used for selling this tool. It is free to use, install, and share, but no profit can be made without my consent. Free open source can use this tool to build other tools but cannot include the code part with the FfeD algorithm I developed. Anyone who wants to use the algorithm needs to contact and communicate with neural_network@brain.scrde.ca. Otherwise, everything else is free to use or sell, including the mathematics in the phi framework.
