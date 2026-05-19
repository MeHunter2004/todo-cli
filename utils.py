def print_tasks(tasks):

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        status = "✅" if task["completed"] else "❌"
        print(f"{task['id']}. {task['title']} [{status}]")
