import json
import os

from configs import configure_argument_parser


class Task:
    def __init__(self, id, title, description, category, due_date, priority,
                 status):
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status
        }


class TaskManager:
    db = 'tasks.json'

    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.db):
            with open(self.db, 'r', encoding='utf-8') as file:
                try:
                    return [Task(**task) for task in json.load(file)]
                except json.JSONDecodeError:
                    return []
        return []

    def save_tasks(self):
        with open(self.db, 'w', encoding='utf-8') as file:
            json.dump([task.to_dict() for task in self.tasks], file,
                      indent=2,
                      ensure_ascii=False)

    def add_task_id(self):
        if not self.tasks:
            return 1
        else:
            return max(task.id for task in self.tasks) + 1

    def add_task(self, title, description, category,
                 due_date, priority, status):
        task = Task(
            id=self.add_task_id(),
            title=title,
            description=description,
            category=category,
            due_date=due_date,
            priority=priority,
            status=status
        )
        self.tasks.append(task)
        self.save_tasks()

    def list_task(self):
        if not self.tasks:
            print('Задачи не найдены')
        else:
            for task in self.tasks:
                print(
                    f'id – {task.id}, '
                    f'название – {task.title}, '
                    f'описание – {task.description}, '
                    f'категория – {task.category}, '
                    f'срок выполнения – {task.due_date}, '
                    f'приоритет – {task.priority}, '
                    f'статус – {task.status}'
                )

    def remove_task(self, id=None, category=None):
        if id is not None:
            for task in self.tasks:
                if task.id == id:
                    self.tasks.remove(task)
                    break
        else:
            for task in self.tasks:
                if task.category == category:
                    self.tasks.remove(task)
        self.save_tasks()

    def search_task(self):
        pass


def main():
    arg_parser = configure_argument_parser()
    args = arg_parser.parse_args()
    manager = TaskManager()
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
        manager.list_task()
    elif args.command == 'remove':
        manager.remove_task(id=args.id, category=args.category)
    elif args.command == 'search':
        print(args)


if __name__ == '__main__':
    main()
