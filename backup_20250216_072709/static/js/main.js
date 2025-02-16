document.addEventListener('DOMContentLoaded', function() {
    // Task Management
    const addTaskForm = document.getElementById('add-task-form');
    const taskList = document.getElementById('task-list');

    addTaskForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const title = document.getElementById('task-title').value;
        const dueDate = document.getElementById('task-due-date').value;
        const priority = document.getElementById('task-priority').value;
        const projectId = document.getElementById('task-project').value;

        // Add task to the list
        const taskItem = document.createElement('li');
        taskItem.textContent = `${title} - ${dueDate} - ${priority}`;
        taskList.appendChild(taskItem);

        // Clear the form
        addTaskForm.reset();

        // Send task data to the server
        fetch('/tasks', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ title, dueDate, priority, projectId })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Task added:', data);
        })
        .catch(error => {
            console.error('Error adding task:', error);
        });
    });

    // Project Categorization
    const addProjectForm = document.getElementById('add-project-form');
    const projectList = document.getElementById('project-list');

    addProjectForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const name = document.getElementById('project-name').value;
        const description = document.getElementById('project-description').value;

        // Add project to the list
        const projectItem = document.createElement('li');
        projectItem.textContent = `${name} - ${description}`;
        projectList.appendChild(projectItem);

        // Clear the form
        addProjectForm.reset();

        // Send project data to the server
        fetch('/projects', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name, description })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Project added:', data);
        })
        .catch(error => {
            console.error('Error adding project:', error);
        });
    });

    // User Registration
    const registerForm = document.getElementById('register-form');
    if (registerForm) {
        registerForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            fetch('/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username, password })
            })
            .then(response => response.json())
            .then(data => {
                console.log('User registered:', data);
                // Redirect to login page or main page
                window.location.href = '/login';
            })
            .catch(error => {
                console.error('Error registering user:', error);
            });
        });
    }

    // User Login
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            fetch('/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username, password })
            })
            .then(response => response.json())
            .then(data => {
                console.log('User logged in:', data);
                // Store the token and redirect to the main page
                localStorage.setItem('token', data.token);
                window.location.href = '/';
            })
            .catch(error => {
                console.error('Error logging in user:', error);
            });
        });
    }
});
