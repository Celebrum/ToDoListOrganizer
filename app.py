import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS

from src.project_manager import ProjectManager
from src.task_manager import TaskManager
from src.user_auth import UserAuth

load_dotenv()

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

# Initialize managers
user_auth = UserAuth()
task_manager = TaskManager()
project_manager = ProjectManager()

# User routes
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
        user = user_auth.register(data['username'], data['password'])
        return jsonify(user), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        token = user_auth.login(data['username'], data['password'])
        return jsonify({"token": token}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 401

# Task routes
@app.route('/api/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'POST':
        data = request.get_json()
        try:
            task = task_manager.add_task(
                data['title'],
                data['due_date'],
                data['priority'],
                data['project_id']
            )
            return jsonify({
                "id": task.id,
                "title": task.title,
                "due_date": task.due_date,
                "priority": task.priority,
                "project_id": task.project_id,
                "completed": task.completed
            }), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
    else:
        tasks = [{"id": t.id, "title": t.title, "due_date": t.due_date, 
                 "priority": t.priority, "project_id": t.project_id, 
                 "completed": t.completed} for t in task_manager.tasks.values()]
        return jsonify(tasks), 200

# Project routes
@app.route('/api/projects', methods=['GET', 'POST'])
def projects():
    if request.method == 'POST':
        data = request.get_json()
        try:
            project = project_manager.add_project(
                data['name'],
                data['description']
            )
            return jsonify({
                "id": project.id,
                "name": project.name,
                "description": project.description
            }), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
    else:
        projects = [{"id": p.id, "name": p.name, "description": p.description} 
                   for p in project_manager.projects.values()]
        return jsonify(projects), 200

if __name__ == '__main__':
    app.run(debug=True)