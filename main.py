import argparse
from task_manager import TaskManager
from utils import print_tasks


def main():

    parser = argparse.ArgumentParser(description="CLI To-Do List")

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title")

    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("id", type=int)

    complete_parser = subparsers.add_parser("complete")
    complete_parser.add_argument("id", type=int)

    subparsers.add_parser("list")

    args = parser.parse_args()

    manager = TaskManager()

    if args.command == "add":
        manager.add_task(args.title)
        print("Task added.")

    elif args.command == "delete":
        manager.delete_task(args.id)
        print("Task deleted.")

    elif args.command == "complete":
        manager.complete_task(args.id)
        print("Task marked as completed.")

    elif args.command == "list":
        tasks = manager.list_tasks()
        print_tasks(tasks)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
