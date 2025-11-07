class Project:
    """
    Represents a project that belongs to a user and contains tasks.

    Attributes:
        title (str): Title of the project.
        description (str): A short explanation of the project.
        due_date (str): Optional due date in string format (YYYY-MM-DD or freeform).
        tasks (list): A list of Task objects associated with this project.
    """

    def __init__(self, title: str, description: str = "", due_date: str = ""):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = []  # One-to-many: Project -> Tasks

    def __str__(self):
        return f"Project(title='{self.title}', due_date='{self.due_date}')"
