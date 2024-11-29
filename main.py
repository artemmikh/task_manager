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
    def __init__(self):
        self.db = 'tasks.json'
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.db):
            with open(self.db, 'r', encoding='utf-8') as file:
                return [Task(**task) for task in json.load(file)]
        else:
            return []

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def save_tasks(self):
        with open(self.db, 'w', encoding='utf-8') as file:
            json.dump([task.to_dict() for task in self.tasks], file,
                      indent=2,
                      ensure_ascii=False)


def main():
    arg_parser = configure_argument_parser()
    args = arg_parser.parse_args()
    print(args)
    manager = TaskManager()
    manager.add_task(Task(id=args.id, title=args.title))


if __name__ == '__main__':
    main()
