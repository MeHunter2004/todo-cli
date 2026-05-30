# To-Do CLI App

A clean and modular command-line To-Do List application built with **Python**, enhanced with **Typer** for a modern CLI experience and **Rich** for beautiful terminal output.

This project is designed as a portfolio-friendly example of writing clean, maintainable, and structured Python code using a layered architecture.

---

## Features

- Add new tasks
- List all tasks in a formatted table
- Mark tasks as completed
- Delete tasks
- Persist tasks using JSON storage
- Clean modular architecture
- User-friendly CLI powered by Typer
- Colored terminal output with Rich

---

## Technologies Used

- **Python**
- **Typer**
- **Rich**
- **JSON** for lightweight data persistence

---

## Project Structure
```bash
todo-cli/
│
├── data/
│   ├── tasks.json
│   └── tasks.sample.json
│
├── main.py
├── models.py
├── storage.py
├── task_manager.py
├── utils.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/MeHunter2004/todo-cli.git
cd todo-cli
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

---

## Usage

### Show help
```bash
python main.py --help
```

### Add a task
```bash
python main.py add "task"
```

### List all tasks
```bash
python main.py list
```

### Mark as completed
```bash
python main.py complete 1
```

### delete a task
```bash
python main.py delete 1
```

---

## Example Workflow
```bash
python main.py add "Study Python"
python main.py add "Go to Gym"
python main.py list
python main.py complete 1
python main.py delete 1
```

---

## Architecture

This project follows a simple layered architecture:

### 1. CLI layer

Handled in main.py using Typer.
Responsible for:
- parsing commands
- receiving user input
- callig the appropriate business logic

### 2. Business Logic Layer

Handled in task_manager.py.
Responsible for:
- creating tasks
- deleting tasks
- marking tasks as completed
- managing task IDs

### 3. Data Layer

Handled in storage.py.
Responsible for:
- loading tasks from JSON
- saving tasks to JSON
- handling missing or invalid storage files safely

### 4. Model Layer

Handled in models.py.
Responsible for:
- defining the Task data structure
- converting task objects to and from dictionary format

### 5. Presentation Utilities

Handled in utils.py.
Responsible for:
- displaying task data in a clean table using Rich

---

## Sample Task Format

tasks are stored in JSON format like this:
```jason
[
    {
        "id": 1,
        "description": "Go to gym",
        "completed": false,
        "created_at": "2026-5-29 14:20:10"
    }
]
```

---

## Why This Project Matters

This project demonstrates:

- modular Python development
- separation of concerns
- clean CLI design
- practical file handling with JSON
- improved user experience in terminal applications

It is a great beginner-to-intermediate portfolio project for showcasing Python development skills.

---

## Future Improvements

Possible future upgrades:

- SQLite database integration
- task priorities
- due dates
- filtering tasks by status
- unit testing with Pytest
- packaging the app for installation via pip
- exporting tasks to CSV or Markdown

---

## Requirements

```txt
typer==0.26.3
rich==14.3.2
```

---

## License

This project is open-source and available under the MIT License.

---

## Author

Built with Python as a portfolio project.
