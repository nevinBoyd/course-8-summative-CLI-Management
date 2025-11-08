class User:
    """
    Represents a user who can own one or more projects.

    Attributes:
        name (str): The user's name.
        email (str): The user's email address.
        projects (list): A list of Project objects associated with this user.
    """

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.projects = []  # One-to-many: User -> Projects

    def add_project(self, project):
        """
        Add a Project instance to this user's project list.
        """
        self.projects.append(project)

    def list_projects(self):
        """
        Return a list of the user's projects.
        """
        return self.projects
    
    def __str__(self):
        return f"User(name='{self.name}', email='{self.email}')"