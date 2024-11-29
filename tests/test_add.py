import pytest
import os
import json
from tempfile import NamedTemporaryFile
from main import TaskManager, Task


@pytest.fixture
def temp_db():
    with NamedTemporaryFile(delete=False, suffix='.json') as tmp_file:
        yield tmp_file.name
    os.remove(tmp_file.name)


@pytest.fixture
def data():
    return {
        'title': 'test',
        'description': 'описание',
        'category': 'отладка',
        'due_date': '1234',
        'priority': 'высокий',
        'status': 'выполнена',
    }


def test_add_task(temp_db, monkeypatch, data):
    monkeypatch.setattr(TaskManager, 'db', temp_db)
    manager = TaskManager()

    assert len(manager.tasks) == 0
    manager.add_task(**data)
    assert len(manager.tasks) == 1

    task = manager.tasks[0]
    for key, value in data.items():
        assert getattr(task, key) == value

    with open(temp_db, 'r', encoding='utf-8') as file:
        tasks = json.load(file)
        assert len(tasks) == 1
        data['id'] = 1
        for key, value in tasks[0].items():
            assert data.get(key) == value
