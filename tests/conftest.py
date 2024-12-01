import json

import pytest
import os
from tempfile import NamedTemporaryFile

from main import TaskManager


@pytest.fixture
def data_no_id():
    return {
        'title': 'test',
        'description': 'описание',
        'category': 'отладка',
        'due_date': '1234',
        'priority': 'высокий',
        'status': 'выполнена',
    }


@pytest.fixture
def data_with_id():
    return {
        'id': '1',
        'title': 'test',
        'description': 'описание',
        'category': 'отладка',
        'due_date': '1234',
        'priority': 'высокий',
        'status': 'выполнена',
    }


@pytest.fixture
def temp_db():
    with NamedTemporaryFile(delete=False, suffix='.json') as tmp_file:
        yield tmp_file.name
    os.remove(tmp_file.name)


@pytest.fixture
def populate_db(temp_db, data_with_id):
    with open(temp_db, 'w', encoding='utf-8') as file:
        json.dump([data_with_id], file, ensure_ascii=False, indent=2)
    return populate_db


@pytest.fixture
def task_manager(monkeypatch, temp_db):
    monkeypatch.setattr(TaskManager, 'db', temp_db)
    manager = TaskManager()
    return manager
