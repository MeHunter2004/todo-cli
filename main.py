import typer
from task_manager import TaskManager
from utils import print_tasks, console

app = typer.Typer(help="Professional Todo CLI built with Typer and Rich")
manager = TaskManager()

@app.command()
def add(description: str = typer.Argument(..., help="The task description")):
    """Add a new task to your list."""
    manager.add_task(description)
    console.print(f"[bold green]✓[/bold green] Task added: [white]'{description}'[/white]")

@app.command()
def list():
    """Show all tasks in a beautiful table."""
    tasks = manager.get_all_tasks()
    print_tasks(tasks)

@app.command()
def complete(task_id: int = typer.Argument(..., help="The ID of the task to complete")):
    """Mark a task as done."""
    if manager.mark_completed(task_id):
        console.print(f"[bold green]✓[/bold green] Task [cyan]#{task_id}[/cyan] marked as completed!")
    else:
        console.print(f"[bold red]✗[/bold red] Task [cyan]#{task_id}[/cyan] not found.")

@app.command()
def delete(task_id: int = typer.Argument(..., help="The ID of the task to delete")):
    """Remove a task from the list."""
    if manager.delete_task(task_id):
        console.print(f"[bold red]![/bold red] Task [cyan]#{task_id}[/cyan] deleted.")
    else:
        console.print(f"[bold red]✗[/bold red] Task [cyan]#{task_id}[/cyan] not found.")

if __name__ == "__main__":
    app()
