import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS

from src.project_manager import ProjectManager
from src.task_manager import TaskManager

load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize managers
task_manager = TaskManager()
project_manager = ProjectManager()

@app.route('/api/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'POST':
        data = request.get_json()
        task = task_manager.add_task(
            data['title'],
            data['due_date'],
            data['priority'],
            data.get('project_id')
        )
        return jsonify({
            "id": task.id,
            "title": task.title,
            "due_date": task.due_date,
            "priority": task.priority
        }), 201
    
    tasks = task_manager.tasks.values()
    return jsonify([{
        "id": t.id,
        "title": t.title,
        "due_date": t.due_date,
        "priority": t.priority
    } for t in tasks]), 200

@app.route('/api/projects', methods=['GET', 'POST'])
def projects():
    if request.method == 'POST':
        data = request.get_json()
        project = project_manager.add_project(
            data['name'],
            data['description']
        )
        return jsonify({
            "id": project.id,
            "name": project.name
        }), 201
    
    projects = project_manager.projects.values()
    return jsonify([{
        "id": p.id,
        "name": p.name
    } for p in projects]), 200

if __name__ == '__main__':
    app.run(debug=True)