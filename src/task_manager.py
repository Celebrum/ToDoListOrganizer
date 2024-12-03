class Task:
    def __init__(self, title, due_date, priority, project_id):
        self.title = title
        self.due_date = due_date
        self.priority = priority
        self.project_id = project_id
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.task_id_counter = 1

    def add_task(self, title, due_date, priority, project_id):
        task = Task(title, due_date, priority, project_id)
        task.id = self.task_id_counter
        self.task_id_counter += 1
        self.tasks.append(task)
        self.integrate_ffed_for_task(task)
        return task

    def edit_task(self, task_id, title, due_date, priority):
        task = self.get_task_by_id(task_id)
        if task:
            task.title = title
            task.due_date = due_date
            task.priority = priority
        return task

    def mark_task_complete(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = True
        return task

    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def get_tasks_by_project(self, project_id):
        return [task for task in self.tasks if task.project_id == project_id]

    def integrate_ffed_for_task(self, task):
        # Placeholder for integrating FfeD framework for task prediction
        pass

    def gather_information_for_task(self, task):
        # Placeholder for automatically gathering information for new tasks
        pass

    def validate_task_data(self, task):
        # Input validation
        if not task.title or not task.due_date or not task.priority:
            raise ValueError("Task data is incomplete")
        # Database constraints
        if task.priority not in ["Low", "Medium", "High"]:
            raise ValueError("Invalid priority value")
        # Data cleaning
        task.title = task.title.strip()
        task.due_date = task.due_date.strip()
        task.priority = task.priority.strip()

    def validate_all_tasks(self):
        for task in self.tasks:
            self.validate_task_data(task)
