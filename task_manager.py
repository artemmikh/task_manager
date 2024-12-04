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

    def list_task(self, all: bool = False,
                  category: Optional[str] = None) -> None:
        """Отображает список всех задач или по категории."""
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

    def remove_task(self, id: Optional[int] = None,
                    category: Optional[str] = None) -> None:
        """Удаляет задачи по ID или категории."""
        if id is not None:
            for task in self.tasks:
                if task.id == id:
                    self.tasks.remove(task)
                    print(f'Задача с ID "{id}" удалена')
                    break
        elif category is not None:
            for task in self.tasks:
                if task.category == category:
                    self.tasks.remove(task)
            print(f'Все задачи с категорией "{category}" удалены')
        self.save_tasks()

    def search_task(
            self,
            keyword: Optional[str] = None,
            category: Optional[str] = None,
            status: Optional[str] = None
    ) -> None:
        """Ищет задачи по ключевому слову, категории или статусу."""
        temp_tasks: List[Task] = []
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

    def edit_task(self, id: int, **kwargs: Union[str, None]) -> None:
        """Редактирует задачу по ID."""
        try:
            task_to_edit: Task = next(
                task for task in self.tasks if task.id == id)
        except StopIteration:
            print('Задача с этим ID не найдена')
            return
        for key, value in kwargs.items():
            if value is not None and hasattr(task_to_edit, key):
                setattr(task_to_edit, key, value)
        if self.validate_task(task_to_edit) is None:
            return
        self.save_tasks()
        print('Задача изменена')
