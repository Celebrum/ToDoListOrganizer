from flask import Flask, request, jsonify
from src.task_manager import TaskManager
from src.user_auth import UserAuth
from src.project_manager import ProjectManager
from src.ffed_framework import FfeDFramework
from src.power_automate_flow import PowerAutomateFlow
from src.gpt2_flask_api import GPT2FlaskAPI

app = Flask(__name__)

task_manager = TaskManager()
user_auth = UserAuth()
project_manager = ProjectManager()
ffed_framework = FfeDFramework()
power_automate_flow = PowerAutomateFlow()
gpt2_flask_api = GPT2FlaskAPI()

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = task_manager.add_task(data['title'], data['due_date'], data['priority'], data['project_id'])
    # Integrate FfeD framework for task prediction and information gathering
    ffed_framework.prediction_system()
    ffed_framework.search_and_scrape()
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def edit_task(task_id):
    data = request.get_json()
    task = task_manager.edit_task(task_id, data['title'], data['due_date'], data['priority'])
    return jsonify(task), 200

@app.route('/tasks/<int:task_id>/complete', methods=['PUT'])
def mark_task_complete(task_id):
    task = task_manager.mark_task_complete(task_id)
    return jsonify(task), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task_manager.delete_task(task_id)
    return '', 204

@app.route('/projects', methods=['POST'])
def add_project():
    data = request.get_json()
    project = project_manager.add_project(data['name'], data['description'])
    # Integrate FfeD framework for project prediction and information gathering
    ffed_framework.prediction_system()
    ffed_framework.search_and_scrape()
    return jsonify(project), 201

@app.route('/projects/<int:project_id>', methods=['PUT'])
def edit_project(project_id):
    data = request.get_json()
    project = project_manager.edit_project(project_id, data['name'], data['description'])
    return jsonify(project), 200

@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    project_manager.delete_project(project_id)
    return '', 204

@app.route('/projects/<int:project_id>/tasks', methods=['GET'])
def get_tasks_by_project(project_id):
    tasks = task_manager.get_tasks_by_project(project_id)
    return jsonify(tasks), 200

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = user_auth.register(data['username'], data['password'])
    return jsonify(user), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    token = user_auth.login(data['username'], data['password'])
    return jsonify({'token': token}), 200

@app.route('/automate', methods=['POST'])
def automate():
    data = request.get_json()
    power_automate_flow.run_flow(data)
    return jsonify({'status': 'Automation started'}), 200

@app.route('/generate_content', methods=['POST'])
def generate_content():
    data = request.get_json()
    prompt = data.get('prompt', '')

    # Generate content using GPT-2
    content = gpt2_flask_api.generate_content(prompt)
    return jsonify({'content': content, 'opposite_synonym_subject': opposite_synonym_subject}), 200

def get_opposite_synonym_subject(last_saved_entry):
    # Placeholder function to get the opposite of the synonym of the last subject
    # Implement the logic to find the opposite synonym subject
    return "opposite_synonym_subject"

if __name__ == '__main__':
    app.run(debug=True)
