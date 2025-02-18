from .domain.healthcare_models import ClinicalPriority, HealthcareContext
from .ffed_framework import FfeDFramework
from .gpt2_flask_api import GPT2FlaskAPI

class Task:
    def __init__(self, id, title, due_date, priority, project_id):
        self.id = id
        self.title = title
        self.due_date = due_date
        self.priority = priority
        self.project_id = project_id
        self.completed = False
        self.healthcare_context = None
        self.clinical_priority = None
        self.research_domain = None
        self.evidence_base = []

class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1
        self.ffed_framework = FfeDFramework()
        self.gpt2_flask_api = GPT2FlaskAPI()

    def add_task(self, title, due_date, priority, project_id):
        task = Task(self.next_id, title, due_date, priority, project_id)
        self.tasks[self.next_id] = task
        self.next_id += 1
        self.integrate_ffed_for_task(task)
        self.gather_information_for_task(task)
        return task

    def edit_task(self, task_id, title, due_date, priority):
        if task_id not in self.tasks:
            raise ValueError("Task not found")
        task = self.tasks[task_id]
        task.title = title
        task.due_date = due_date
        task.priority = priority
        return task

    def mark_task_complete(self, task_id):
        if task_id not in self.tasks:
            raise ValueError("Task not found")
        task = self.tasks[task_id]
        task.completed = True
        return task

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]

    def get_task_by_id(self, task_id):
        return self.tasks.get(task_id)

    def get_tasks_by_project(self, project_id):
        return [task for task in self.tasks.values() if task.project_id == project_id]

    def integrate_ffed_for_task(self, task):
        self.ffed_framework.prediction_system()
        self.ffed_framework.search_and_scrape()

    def gather_information_for_task(self, task):
        prompt = f"Generate content for task: {task.title}"
        response = self.gpt2_flask_api.generate_content({"prompt": prompt})
        task.generated_content = response.get('content', '')

    def validate_task_data(self, task):
        if not task.title or not task.due_date or not task.priority:
            raise ValueError("Task data is incomplete")
        if task.priority not in ["Low", "Medium", "High"]:
            raise ValueError("Invalid priority value")
        task.title = task.title.strip()
        task.due_date = task.due_date.strip()
        task.priority = task.priority.strip()

    def validate_all_tasks(self):
        for task in self.tasks.values():
            self.validate_task_data(task)

    def add_healthcare_context(self, task_id, context: HealthcareContext, 
                             clinical_priority: ClinicalPriority = None):
        task = self.get_task_by_id(task_id)
        if task:
            task.healthcare_context = context
            task.clinical_priority = clinical_priority
            return task
        raise ValueError("Task not found")

    def add_evidence(self, task_id, evidence_data):
        task = self.get_task_by_id(task_id)
        if task:
            task.evidence_base.append(evidence_data)
            return task
        raise ValueError("Task not found")
