import json
from typing import Dict

import pytest

from services.task_manager import TaskManager


@pytest.mark.parametrize(
    'edit_param',
    [
        ({'title': 'изменённая задача', 'id': 1}),
        ({'status': 'выполнена', 'id': 1, }),
        ({'priority': 'средний', 'category': 'исследование', 'id': 1})
    ]
)
def test_edit_task(
        edit_param: Dict[str, str],
        populate_db: None, task_manager: TaskManager) -> None:
    """Тестирует изменение задачи."""
    task_manager.edit_task(**edit_param)
    with open(task_manager.db, 'r', encoding='utf-8') as file:
        tasks = json.load(file)
        updated_task = next(
            task for task in tasks if task['id'] == edit_param['id'])
        for key, value in edit_param.items():
            assert updated_task[key] == value


@pytest.mark.parametrize(
    'edit_param',
    [
        ({'title': 'новая задача', 'id': 1}),
    ]
)
def test_edit_task_invalid_id(
        edit_param: Dict[str, str],
        task_manager: TaskManager, capsys: pytest.CaptureFixture) -> None:
    """Тестирует изменение задачи с несуществующим ID."""
    task_manager.edit_task(**edit_param)
    output = capsys.readouterr()
    assert output.out.strip() == 'Задача с этим ID не найдена'
