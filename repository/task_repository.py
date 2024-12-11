import json
import os
from typing import List

from models.task import Task


class TaskRepository:
    """Класс для работы с базой данных задач."""

    def __init__(self, db_path: str = 'tasks.json') -> None:
        self.db_path = db_path

    def load_tasks(self) -> List[Task]:
        """Загружает задачи из файла базы данных."""
        if os.path.exists(self.db_path):
            with open(self.db_path, 'r', encoding='utf-8') as file:
                try:
                    return [Task(**task) for task in json.load(file)]
                except json.JSONDecodeError:
                    return []
        return []

    def save_tasks(self, tasks: List[Task]) -> None:
        """Сохраняет текущие задачи в файл базы данных."""
        with open(self.db_path, 'w', encoding='utf-8') as file:
            json.dump([task.to_dict() for task in tasks], file,
                      indent=2,
                      ensure_ascii=False)
