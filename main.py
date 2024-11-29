import json
import os

from configs import configure_argument_parser


class Task:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title
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

    def add_task(self, title):
        task = Task(id=self.add_task_id(), title=title)
        self.tasks.append(task)
        self.save_tasks()

    def list_task(self):
        if not self.tasks:
            print('Задачи не найдены')
        else:
            for task in self.tasks:
                print(f'id – {task.id}, название – {task.title}')


def main():
    arg_parser = configure_argument_parser()
    args = arg_parser.parse_args()
    manager = TaskManager()
    if args.command == 'add':
        manager.add_task(title=args.title)
    elif args.command == 'list':
        manager.list_task()


if __name__ == '__main__':
    main()
