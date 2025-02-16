# Project Structure

## Directory and File Structure

The ToDoListOrganizer project is organized into the following directories and files:

```
to_do_organizer/
│
├── src/
│   ├── app.py              # Main entry point of the application
│   ├── task_manager.py     # Handles all task-related operations
│   ├── user_auth.py        # Handles user registration and login
│   └── project_manager.py  # Manages project-related operations
│
├── templates/              # HTML templates for user interface (if web-based)
│   ├── index.html
│   ├── login.html
│   └── project_view.html
│
├── static/                 # Static files like CSS and JavaScript
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
│
├── tests/                  # Unit and integration tests
│   ├── test_task_manager.py
│   ├── test_user_auth.py
│   └── test_project_manager.py
│
└── README.md               # Documentation for setup and usage
```

## Description of Key Files

### `src/app.py`
- The main entry point of the application. It initializes the Flask app, sets up routes, and starts the server.

### `src/task_manager.py`
- Handles all task-related operations, including adding, editing, marking complete, and deleting tasks.

### `src/user_auth.py`
- Manages user registration and login, including JWT token generation and validation.

### `src/project_manager.py`
- Manages project-related operations, including adding, editing, and deleting projects.

### `templates/`
- Contains HTML templates for the user interface if the application is web-based.

### `static/`
- Contains static files like CSS and JavaScript for the user interface.

### `tests/`
- Contains unit and integration tests for the application.

### `README.md`
- Provides documentation for setting up and using the application.

## Note on FfeD Algorithm

Please protect the FfeD algorithm but share as much knowledge on the phi framework. The rest is all free to be shared, but because of the FfeD framework, it cannot be used for selling this tool. It is free to use, install, and share, but no profit can be made without my consent. Free open source can use this tool to build other tools but cannot include the code part with the FfeD algorithm I developed. Anyone who wants to use the algorithm needs to contact and communicate with neural_network@brain.scrde.ca. Otherwise, everything else is free to use or sell, including the mathematics in the phi framework.
