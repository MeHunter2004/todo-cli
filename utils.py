from rich.console import Console
from rich.table import Table
from typing import List
from models import Task

console = Console()

def print_tasks(tasks: List[Task]):
    if not tasks:
        console.print("[yellow]No tasks found. Add one with 'add' command![/yellow]")
        return

    table = Table(title="📝 My To-Do List", header_style="bold magenta")
    
    table.add_column("ID", justify="center", style="cyan", no_wrap=True)
    table.add_column("Description", style="white")
    table.add_column("Status", justify="center")
    table.add_column("Created At", style="dim")

    for task in tasks:
        status = "[green]✅ Done[/green]" if task.completed else "[yellow]⏳ Pending[/yellow]"
        table.add_row(str(task.id), task.description, status, task.created_at)

    console.print(table)
