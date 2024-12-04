import json
from typing import Dict

from task_manager import TaskManager


def test_add_task(temp_db: str, task_manager: TaskManager,
                  data_no_id: Dict[str, str]) -> None:
    """Тестирует добавление задачи."""
    assert len(task_manager.tasks) == 0
    task_manager.add_task(**data_no_id)
    assert len(task_manager.tasks) == 1

    task = task_manager.tasks[0]
    for key, value in data_no_id.items():
        assert getattr(task, key) == value

    with open(temp_db, 'r', encoding='utf-8') as file:
        tasks = json.load(file)
        assert len(tasks) == 1
        data_no_id['id'] = 1
        for key, value in tasks[0].items():
            assert data_no_id.get(key) == value
