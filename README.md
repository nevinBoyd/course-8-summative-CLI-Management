# Summative Project: Python Project Management CLI Tool

## Learning Goals

* Build structured and user-friendly command-line applications using `argparse`.
* Apply object-oriented programming (OOP) to real-world modeling.
* Manage one-to-many relationships between Users → Projects → Tasks.
* Persist application data locally using JSON and file I/O.
* Use external packages (e.g., `rich`) to improve CLI output quality.
* Follow modular code organization for maintainability and clarity.

---

## Project Overview

This project implements a Python-based Command-Line Interface (CLI) application designed to simulate a multi-user project tracker system. Administrators can create and list users, add projects to users, add tasks to projects, and mark tasks complete. Data persists locally to `data/data.json` so the application state survives between runs.

The system models real collaborative workflows where multiple contributors manage multiple projects, each containing its own tasks. The design emphasizes clarity, modularity, and scalability.

---

## File Structure

```
COURSE-8-SUMMATIVE-CLI-MANAGEMENT
├── data/
│   └── data.json
├── models/
│   ├── __init__.py
│   ├── user.py        
│   ├── project.py    
│   └── task.py        
├── utils/
│   ├── __init__.py
│   └── persistence.py # Load/save JSON helpers
├── tests/
│   ├── __init__.py
│   ├── test_user.py
│   ├── test_project.py
│   └── test_task.py
├── venv/              # (optional) virtual environment (ignored in git)
├── main.py            
├── requirements.txt   
└── README.md
```

---

## Setup Instructions

### 1. Clone the Repository

```
git clone <repo-url>
cd COURSE-8-SUMMATIVE-CLI-MANAGEMENT
```

### 2. Create and Activate Virtual Environment 

**macOS / Linux**
```
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell)**
```
python -m venv venv
venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

> The project uses:
>
> * `rich` for pretty terminal tables and formatting (documented in `requirements.txt`).

### 4. Verify Python Version

This project targets **Python 3.10+** 
```
python3 --version
```

### 5. Ensure Data File Exists

If `data/data.json` does not exist, create it:
```
mkdir -p data
echo '{"users": []}' > data/data.json
```

---

## How to Run / CLI Commands

Usage pattern:
```
python3 main.py <command> [--flags]
```

Available commands:

* `add-user --name "Name" --email "email@eaxample.com"`
  Adds a new user.

* `list-users`
  Lists all users in a table.

* `add-project --user "Name" --title "Project Title" [--description "desc"] [--due "YYYY-MM-DD"]`
  Adds a project under a user.

* `list-projects --user "Name"`
  Lists all projects for a user.

* `add-task --user "Name" --project "Project Title" --title "Task Title"`
  Adds a task to a project.

* `list-tasks --user "Name" --project "Project Title"`
  Lists tasks for a project.

* `complete-task --user "Name" --project "Project Title" --title "Task Title"`
  Marks a task as complete.

Examples:
```
python3 main.py add-user --name "Alex" --email "alex@example.com"
python3 main.py add-project --user "Alex" --title "CLI Tool" --description "Build CLI" --due "2026-01-01"
python3 main.py add-task --user "Alex" --project "CLI Tool" --title "Implement add-task"
python3 main.py list-projects --user "Alex"
python3 main.py complete-task --user "Alex" --project "CLI Tool" --title "Implement add-task"
```

---

## Design Notes

* **Models**: `User`, `Project`, `Task` are implemented in `models/` with simple attributes and helper methods (e.g., `mark_complete`, `add_project`, `add_task`).
* **Persistence**: `utils/persistence.py` handles JSON load/save with safe error handling for missing or malformed files.
* **CLI**: `main.py` uses `argparse` with `subparsers` to route commands to functions.
* **External package**: `rich` provides clean terminal tables and colored messages.

---

## Testing

* Tests exist in `tests/` (pytest). Example command:
  ```
  pytest -q
  ```

The project includes tests in the `tests/` directory. These tests verify:

* Creation and behavior of the `User`, `Project`, and `Task` classes.
* JSON persistence via the load/save helpers.
* CLI command execution (with controlled input/output).
---

## Resources

*  [https://www.python.org/](https://www.python.org/)
*  [https://docs.python.org/3/library/index.html](https://docs.python.org/3/library/index.html)
*  [https://code.visualstudio.com/](https://code.visualstudio.com/)
*  [https://github.com/](https://github.com/)
*  [https://rich.readthedocs.io/en/latest/introduction.html](https://rich.readthedocs.io/en/latest/introduction.html)
*  [https://www.makeareadme.com/](https://www.makeareadme.com/)

---

## Known Issues / Notes

* The `data/data.json` file is included in version control to provide an example dataset. 
If desired, temporary or backup files (e.g., `*.bak`, `*.tmp`) can be added to `.gitignore`.
* The CLI stores user and project names case-insensitively when searching but preserves original casing when listing.
* If you experience inconsistent behavior after editing `main.py`, ensure the virtual environment is activated and you’re running `python3 main.py ...` from project root.

---

## Learning & Takeaways

* Building a modular CLI helps separate concerns: models, utils, CLI controller.
* JSON-backed persistence is a light-weight way to simulate an app database
* `argparse` + `rich` gives a strong developer UX for small tools.
* Tests and consistent commits make the project reproducible and easy to review.


























