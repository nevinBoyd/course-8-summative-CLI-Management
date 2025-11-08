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

    args = parser.parse_args()

    if args.command == "add-user":
        add_user(args.name, args.email)

    elif args.command == "list-users":
        list_users()

    elif args.command == "add-project":
        add_project(args.user, args.title, args.description, args.due)

    elif args.command == "list-projects":
        list_projects(args.user)
    

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
