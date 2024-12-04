from argparse import Namespace

from configs import configure_argument_parser
from task_manager import TaskManager


def main() -> None:
    arg_parser = configure_argument_parser()
    args: Namespace = arg_parser.parse_args()
    manager: TaskManager = TaskManager()

    if args.command == 'add':
        manager.add_task(
            title=args.title,
            description=args.description,
            category=args.category,
            due_date=args.due_date,
            priority=args.priority,
            status=args.status,
        )
    elif args.command == 'list':
        manager.list_task(all=args.all, category=args.category)
    elif args.command == 'remove':
        manager.remove_task(id=args.id, category=args.category)
    elif args.command == 'search':
        manager.search_task(keyword=args.keyword, category=args.category,
                            status=args.status)
    elif args.command == 'edit':
        manager.edit_task(
            id=args.id,
            title=args.title,
            description=args.description,
            category=args.category,
            due_date=args.due_date,
            priority=args.priority,
            status=args.status,
        )


if __name__ == '__main__':
    main()
