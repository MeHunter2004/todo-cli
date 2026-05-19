# 📝 Todo CLI

A simple and modular command-line To‑Do List application built with Python.

This project demonstrates clean code structure, layered architecture, and JSON-based data persistence.

---

## ✨ Features

- Add new tasks
- List all tasks
- Mark tasks as completed
- Delete tasks
- Persistent storage using JSON

---

## 🧱 Architecture

The project follows a simple layered structure:

- `main.py` → CLI layer (argparse)
- `task_manager.py` → Business logic
- `storage.py` → JSON persistence
- `models.py` → Task data model
- `utils.py` → Helper functions

This separation improves readability, maintainability, and extensibility.

---

## 🚀 Usage

Run from the project root:
python main.py <command>
# ➕ Add a Task
python main.py add "Buy groceries"
# 📋 List Tasks
bash
python main.py list
# ✅ Complete a Task
bash
python main.py complete 1
# ❌ Delete a Task
bash
python main.py delete 1

---

## 🛠 Tech Stack
Python 3
argparse
JSON
dataclasses

---

## 👤 Author
Computer Engineering Student | Python Developer

## If you find this useful, feel free to ⭐ the repository.

`
