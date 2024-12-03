import json
import os
import time

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

    def get_output_format(self, tasks):
        return '\n'.join(
            f'id – {task.id}, '
            f'название – {task.title}, '
            f'описание – {task.description}, '
            f'категория – {task.category}, '
            f'срок выполнения – {task.due_date}, '
            f'приоритет – {task.priority}, '
            f'статус – {task.status}'
            for task in tasks
        )

    def validate_task(self, task):
        if task.due_date is not None:
            try:
                time.strptime(task.due_date, "%Y-%m-%d")
            except ValueError:
                print('Ошибка. Пожалуйста, используйте формат даты '
                      'год-месяц-день, например '
                      f'"{time.strftime("%Y-%m-%d", time.localtime())}"')
                return
        return task

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
        task = self.validate_task(task)
        self.tasks.append(task)
        self.save_tasks()
        print(f'Задача добавлена. ID задачи {task.id}')

    def list_task(self, all=False, category=None):
        if not self.tasks:
            print('Задачи не найдены')
        elif all:
            print(self.get_output_format(self.tasks))
        elif category is not None:
            find_category = False
            for task in self.tasks:
                if task.category == category:
                    print(self.get_output_format([task]))
                    find_category = True
            if not find_category:
                print(f'Нет задач в категории "{category}"')

    def remove_task(self, id=None, category=None):
        if id is not None:
            for task in self.tasks:
                if task.id == id:
                    self.tasks.remove(task)
                    print(f'Задача с ID "{id}" удалена')
                    break
        else:
            for task in self.tasks:
                if task.category == category:
                    self.tasks.remove(task)
            print(f'Все задачи с категорией "{category}" удалены')
        self.save_tasks()

    def search_task(self, keyword=None, category=None, status=None):
        temp_tasks = []
        if keyword is not None:
            for task in self.tasks:
                if keyword in task.title or keyword in task.description:
                    temp_tasks.append(task)
                if not temp_tasks:
                    print(f'Задачи с ключевым словом {keyword} не найдены')
        elif category is not None:
            for task in self.tasks:
                if category == task.category:
                    temp_tasks.append(task)
                if not temp_tasks:
                    print(f'Задачи с категорией {category} не найдены')
        elif status is not None:
            for task in self.tasks:
                if task.status == status:
                    temp_tasks.append(task)
                if not temp_tasks:
                    print(f'Задачи с статусом {status} не найдены')
        self.tasks = temp_tasks
        self.list_task(all=True)

    def edit_task(self, id, **kwargs):
        try:
            task_to_edit = next(task for task in self.tasks if task.id == id)
        except StopIteration:
            print('Задача с этим ID не найдена')
            return
        for key, value in kwargs.items():
            if value is not None and hasattr(task_to_edit, key):
                setattr(task_to_edit, key, value)
        self.validate_task(task_to_edit)
        self.save_tasks()
        print('Задача изменена')


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
