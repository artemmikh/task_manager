import json
import os
import time
from typing import List, Optional, Union

from task import Task


class TaskManager:
    """Класс для управления задачами. Обеспечивает операции добавления,
    редактирования, удаления, поиска и отображения задач."""

    db: str = 'tasks.json'

    def __init__(self) -> None:
        """Инициализирует менеджер задач, загружая задачи из файла."""
        self.tasks: List[Task] = self.load_tasks()

    def load_tasks(self) -> List[Task]:
        """Загружает задачи из файла базы данных."""
        if os.path.exists(self.db):
            with open(self.db, 'r', encoding='utf-8') as file:
                try:
                    return [Task(**task) for task in json.load(file)]
                except json.JSONDecodeError:
                    return []
        return []

    def save_tasks(self) -> None:
        """Сохраняет текущие задачи в файл базы данных."""
        with open(self.db, 'w', encoding='utf-8') as file:
            json.dump([task.to_dict() for task in self.tasks], file,
                      indent=2,
                      ensure_ascii=False)

    def add_task_id(self) -> int:
        """Генерирует уникальный идентификатор для новой задачи."""
        if not self.tasks:
            return 1
        else:
            return max(task.id for task in self.tasks) + 1

    def get_output_format(self, tasks: List[Task]) -> str:
        """Форматирует список задач для вывода."""
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

    def validate_task(self, task: Task) -> Optional[Task]:
        """Валидирует задачу, проверяя корректность даты выполнения."""
        if task.due_date is not None:
            try:
                time.strptime(task.due_date, "%Y-%m-%d")
            except ValueError:
                print('Ошибка. Пожалуйста, используйте формат даты '
                      'год-месяц-день, например '
                      f'"{time.strftime("%Y-%m-%d", time.localtime())}"')
                return None
        return task

    def get_tasks_by_criteria(
            self, **criteria: Optional[str]) -> Optional[List[Task]]:
        """Ищет задачи по критериям."""
        filters = {
            'keyword': lambda t, kw: kw in t.title or kw in t.description,
            'category': lambda t, c: t.category == c,
            'status': lambda t, s: t.status == s,
            'id': lambda t, id: t.id == id,
        }
        for key, value in criteria.items():
            if value and key in filters:
                tasks = list(
                    filter(lambda task: filters[key](task, value),
                           self.tasks))
        return tasks

    def add_task(
            self,
            title: str,
            description: str,
            category: str,
            due_date: str,
            priority: str,
            status: str
    ) -> None:
        """Добавляет новую задачу."""
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
        if task:
            self.tasks.append(task)
            self.save_tasks()
            print(f'Задача добавлена. ID задачи {task.id}')

    def list_task(
            self, all: Optional[bool] = False,
            **criteria: Optional[str]) -> None:
        """Отображает список всех задач или по категории."""
        tasks_to_show = self.tasks if all else self.get_tasks_by_criteria(
            **criteria)
        if not tasks_to_show:
            print('Задачи не найдены')
            return
        print(self.get_output_format(tasks_to_show))

    def remove_task(self, **criteria: Optional[str]) -> None:
        """Удаляет задачи по ID или категории."""
        tasks_to_remove: Optional[List[Task]] = self.get_tasks_by_criteria(
            **criteria)
        if not tasks_to_remove:
            print('Задачи для удаления не найдены')
            return
        self.tasks = [task for task in self.tasks if
                      task not in tasks_to_remove]
        self.save_tasks()
        print('Удаление выполнено')

    def search_task(self, **criteria: Optional[str]) -> None:
        tasks = self.get_tasks_by_criteria(**criteria)
        if not tasks:
            print('Задачи не найдены')
        else:
            print(self.get_output_format(tasks))

    def edit_task(self, **criteria: Optional[str]) -> None:
        """Редактирует задачу по ID."""
        task_to_edit: list[Optional[Task]] = self.get_tasks_by_criteria(
            **criteria)
        if not task_to_edit:
            print('Задача с этим ID не найдена')
            return
        task_to_edit: Task = task_to_edit[0]
        for key, value in criteria.items():
            if value is not None and hasattr(task_to_edit, key):
                setattr(task_to_edit, key, value)
        if self.validate_task(task_to_edit) is None:
            return
        self.save_tasks()
        print('Задача изменена')
