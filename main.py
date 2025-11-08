import argparse
from utils.persistence import load_data, save_data
from rich.console import Console
from rich.table import Table
from models.project import Project
from models.user import User

console = Console()

# List all users
def list_users():
    data = load_data()
    users = data.get("users", [])

    if not users:
        console.print("[bold yellow]No users found.[/]")
        return

    table = Table(title="Users")
    table.add_column("Name", style="cyan")
    table.add_column("Email", style="magenta")

    for user in users:
        table.add_row(user["name"], user["email"])

    console.print(table)

# Add a new user
def add_user(name, email):
    data = load_data()

    # Prevent duplicates
    for user in data["users"]:
        if user["name"].lower() == name.lower():
            console.print(f"[bold red]User '{name}' already exists![/]")
            return

    new_user = {
        "name": name,
        "email": email,
        "projects": []
    }

    data["users"].append(new_user)
    save_data(data)
    console.print(f"[bold green]User '{name}' added successfully![/]")

# Add a project to a user
def add_project(user_name, title, description, due_date):
    data = load_data()

    # Find the user
    user = next((u for u in data["users"] if u["name"].lower() == user_name.lower()), None)
    if not user:
        console.print(f"[bold red]User '{user_name}' not found![/]")
        return

    new_project = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "tasks": []
    }

    user["projects"].append(new_project)
    save_data(data)
    console.print(f"[bold green]Project '{title}' added to user '{user_name}'.[/]")

# List all projects for a user
def list_projects(user_name):
    data = load_data()

    user = next((u for u in data["users"] if u["name"].lower() == user_name.lower()), None)
    if not user:
        console.print(f"[bold red]User '{user_name}' not found![/]")
        return

    projects = user.get("projects", [])
    if not projects:
        console.print(f"[yellow]No projects found for '{user_name}'.[/]")
        return

    table = Table(title=f"Projects for {user_name}")
    table.add_column("Title", style="cyan")
    table.add_column("Due Date", style="magenta")
    table.add_column("Description")

    for project in projects:
        table.add_row(project["title"], project["due_date"], project["description"])

    console.print(table)

# Add a task to a project
def add_task(user_name, project_title, task_title):
    data = load_data()

    # Find user
    user = next((u for u in data["users"] if u["name"].lower() == user_name.lower()), None)
    if not user:
        console.print(f"[bold red]User '{user_name}' not found.[/]")
        return

    # Find project
    project = next((p for p in user["projects"] if p["title"].lower() == project_title.lower()), None)
    if not project:
        console.print(f"[bold red]Project '{project_title}' not found for '{user_name}'.[/]")
        return

    new_task = {
        "title": task_title,
        "status": "incomplete",
        "assigned_to": None
    }

    project["tasks"].append(new_task)
    save_data(data)
    console.print(f"[bold green]Task '{task_title}' added to project '{project_title}'.[/]")


# List all tasks in a project
def list_tasks(user_name, project_title):
    data = load_data()

    # Find user
    user = next((u for u in data["users"] if u["name"].lower() == user_name.lower()), None)
    if not user:
        console.print(f"[bold red]User '{user_name}' not found.[/]")
        return

    # Find project
    project = next((p for p in user["projects"] if p["title"].lower() == project_title.lower()), None)
    if not project:
        console.print(f"[bold red]Project '{project_title}' not found for '{user_name}'.[/]")
        return

    tasks = project.get("tasks", [])
    if not tasks:
        console.print(f"[yellow]No tasks found for '{project_title}'.[/]")
        return

    table = Table(title=f"Tasks for {project_title}")
    table.add_column("Title", style="cyan")
    table.add_column("Status", style="magenta")

    for task in tasks:
        table.add_row(task["title"], task["status"])

    console.print(table)

# Mark a task as complete
def complete_task(user_name, project_title, task_title):
    data = load_data()

    # Find user
    user = next((u for u in data["users"] if u["name"].lower() == user_name.lower()), None)
    if not user:
        console.print(f"[bold red]User '{user_name}' not found.[/]")
        return

    # Find project
    project = next((p for p in user["projects"] if p["title"].lower() == project_title.lower()), None)
    if not project:
        console.print(f"[bold red]Project '{project_title}' not found for '{user_name}'.[/]")
        return

    # Find task
    task = next((t for t in project["tasks"] if t["title"].lower() == task_title.lower()), None)
    if not task:
        console.print(f"[bold red]Task '{task_title}' not found.[/]")
        return

    task["status"] = "complete"
    save_data(data)
    console.print(f"[bold green]Task '{task_title}' marked complete![/]")

def main():
    parser = argparse.ArgumentParser(description="Project Management CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    # add-user
    add_user_parser = subparsers.add_parser("add-user", help="Add a new user")
    add_user_parser.add_argument("--name", required=True)
    add_user_parser.add_argument("--email", required=True)

    # list-users
    subparsers.add_parser("list-users", help="List all users")

    # add-project
    add_project_parser = subparsers.add_parser("add-project", help="Add a project to a user")
    add_project_parser.add_argument("--user", required=True)
    add_project_parser.add_argument("--title", required=True)
    add_project_parser.add_argument("--description", default="")
    add_project_parser.add_argument("--due", default="No due date")

    # list-projects
    list_projects_parser = subparsers.add_parser("list-projects", help="List projects for a user")
    list_projects_parser.add_argument("--user", required=True)
    
    # add-task
    add_task_parser = subparsers.add_parser("add-task", help="Add a task to a project")
    add_task_parser.add_argument("--user", required=True)
    add_task_parser.add_argument("--project", required=True)
    add_task_parser.add_argument("--title", required=True)

    # list-tasks
    list_tasks_parser = subparsers.add_parser("list-tasks", help="List tasks for a project")
    list_tasks_parser.add_argument("--user", required=True)
    list_tasks_parser.add_argument("--project", required=True)

    # complete-task
    complete_task_parser = subparsers.add_parser("complete-task", help="Mark a task as complete")
    complete_task_parser.add_argument("--user", required=True)
    complete_task_parser.add_argument("--project", required=True)
    complete_task_parser.add_argument("--title", required=True)

    args = parser.parse_args()

    if args.command == "add-user":
        add_user(args.name, args.email)

    elif args.command == "list-users":
        list_users()

    elif args.command == "add-project":
        add_project(args.user, args.title, args.description, args.due)

    elif args.command == "list-projects":
        list_projects(args.user)
    
    elif args.command == "add-task":
        add_task(args.user, args.project, args.title)

    elif args.command == "list-tasks":
        list_tasks(args.user, args.project)

    elif args.command == "complete-task":
        complete_task(args.user, args.project, args.title)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
