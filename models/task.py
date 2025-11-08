class Task:
    """
    Represents an individual task inside a project.

    Attributes:
        title (str): Name of the task.
        status (str): Either "incomplete" or "complete".
        assigned_to (str|None): Name of the user assigned, optional.
    """

    def __init__(self, title: str, assigned_to: str = None, status: str = "incomplete"):
        self.title = title
        self.assigned_to = assigned_to
        self.status = status
    
    def mark_complete(self):
        """
        Mark this task as complete.
        """
        self.status = "complete"

    def __str__(self):
        return f"Task(title='{self.title}', status='{self.status}', assigned_to='{self.assigned_to}')"
