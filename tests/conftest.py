import json
import os
import time
from tempfile import NamedTemporaryFile
from typing import Dict, List, Union

import pytest

from task_manager import TaskManager

TODAY = time.strftime("%Y-%m-%d", time.localtime())


@pytest.fixture
def formatted_output() -> str:
    """Форматирует список задач для вывода."""

    def formatter(tasks: List[Dict[str, Union[str, int]]]) -> str:
        return '\n'.join(
            f'id – {task["id"]}, '
            f'название – {task["title"]}, '
            f'описание – {task["description"]}, '
            f'категория – {task["category"]}, '
            f'срок выполнения – {task["due_date"]}, '
            f'приоритет – {task["priority"]}, '
            f'статус – {task["status"]}'
            for task in tasks
        )

    return formatter


@pytest.fixture
def data_no_id() -> Dict[str, str]:
    """Возвращает данные для задачи без ID."""
    return {
        'title': 'test',
        'description': 'описание',
        'category': 'отладка',
        'due_date': f'{TODAY}',
        'priority': 'высокий',
        'status': 'выполнена',
    }


@pytest.fixture
def data_with_id() -> List[Dict[str, Union[str, int]]]:
    """Возвращает список задач с ID."""
    return [
        {
            'id': 1,
            'title': 'test',
            'description': 'описание для поиска по ключевым словам',
            'category': 'отладка',
            'due_date': f'{TODAY}',
            'priority': 'высокий',
            'status': 'выполнена',
        },
        {
            'id': 2,
            'title': 'test2',
            'description': 'описание для поиска по ключевым словам 2',
            'category': 'исследование',
            'due_date': f'{TODAY}',
            'priority': 'средний',
            'status': 'не выполнена',
        },
        {
            'id': 3,
            'title': 'test3',
            'description': 'описание 3',
            'category': 'исследование',
            'due_date': f'{TODAY}',
            'priority': 'низкий',
            'status': 'выполнена',
        }
    ]


@pytest.fixture
def temp_db() -> str:
    """Создает временную базу данных и возвращает её путь."""
    with NamedTemporaryFile(delete=False, suffix='.json') as tmp_file:
        yield tmp_file.name
    os.remove(tmp_file.name)


@pytest.fixture
def populate_db(temp_db: str, data_with_id: List[Dict[str, str]]) -> None:
    """Заполняет базу данных тестовыми данными."""
    with open(temp_db, 'w', encoding='utf-8') as file:
        json.dump(data_with_id, file, ensure_ascii=False, indent=2)


@pytest.fixture
def task_manager(monkeypatch, temp_db: str) -> TaskManager:
    """Создает и возвращает экземпляр TaskManager с временной базой данных."""
    monkeypatch.setattr(TaskManager, 'db', temp_db)
    manager = TaskManager()
    return manager
