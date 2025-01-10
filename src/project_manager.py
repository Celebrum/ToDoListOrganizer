class Project:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

class ProjectManager:
    def __init__(self):
        self.projects = {}
        self.next_id = 1

    def add_project(self, name, description):
        project = Project(self.next_id, name, description)
        self.projects[self.next_id] = project
        self.next_id += 1
        return project

    def edit_project(self, project_id, name, description):
        if project_id not in self.projects:
            raise ValueError("Project not found")
        project = self.projects[project_id]
        project.name = name
        project.description = description
        return project

    def delete_project(self, project_id):
        if project_id in self.projects:
            del self.projects[project_id]

    def get_project_by_id(self, project_id):
        return self.projects.get(project_id)

    def integrate_ffed_for_project(self, project):
        # Placeholder for FfeD framework integration
        pass

    def gather_information_for_project(self, project):
        # Placeholder for FfeD framework information gathering
        pass

    def validate_project_data(self, project):
        # Input validation
        if not project.name or not project.description:
            raise ValueError("Project data is incomplete")
        # Data cleaning
        project.name = project.name.strip()
        project.description = project.description.strip()

    def validate_all_projects(self):
        for project in self.projects.values():
            self.validate_project_data(project)
