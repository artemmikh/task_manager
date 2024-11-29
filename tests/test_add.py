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


def test_add_task(temp_db, monkeypatch):
    monkeypatch.setattr(TaskManager, 'db', temp_db)
    manager = TaskManager()

    assert len(manager.tasks) == 0
    
    new_task = Task(id=1, title="Test Task")
    manager.add_task(new_task)

    assert len(manager.tasks) == 1
    assert manager.tasks[0].id == 1
    assert manager.tasks[0].title == "Test Task"

    with open(temp_db, 'r', encoding='utf-8') as file:
        data = json.load(file)
        assert len(data) == 1
        assert data[0]['id'] == 1
        assert data[0]['title'] == "Test Task"
