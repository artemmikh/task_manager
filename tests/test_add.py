import json

from main import TaskManager


def test_add_task(temp_db, monkeypatch, data_no_id):
    monkeypatch.setattr(TaskManager, 'db', temp_db)
    manager = TaskManager()

    assert len(manager.tasks) == 0
    manager.add_task(**data_no_id)
    assert len(manager.tasks) == 1

    task = manager.tasks[0]
    for key, value in data_no_id.items():
        assert getattr(task, key) == value

    with open(temp_db, 'r', encoding='utf-8') as file:
        tasks = json.load(file)
        assert len(tasks) == 1
        data_no_id['id'] = 1
        for key, value in tasks[0].items():
            assert data_no_id.get(key) == value
