from typing import List, Dict, Union

import pytest

from services.task_manager import TaskManager


def test_empty_list_task(
        task_manager: TaskManager, capsys: pytest.CaptureFixture) -> None:
    """Тестирует вывод списка задач при их отсутствии."""
    task_manager.list_task(all=True)
    output = capsys.readouterr()
    assert output.out.strip() == 'Задачи не найдены'


def test_list_all_task(
        capsys: pytest.CaptureFixture, populate_db: None,
        data_with_id: List[Dict[str, Union[str, int]]], task_manager:
        TaskManager,
        formatted_output: callable) -> None:
    """Тестирует вывод списка всех задач."""
    task_manager.list_task(all=True)
    output = capsys.readouterr()
    expected_output = formatted_output(data_with_id)
    assert output.out.strip() == expected_output


def test_list_task_by_category(
        capsys: pytest.CaptureFixture, populate_db: None,
        data_with_id: List[Dict[str, Union[str, int]]],
        task_manager: TaskManager,
        formatted_output: callable) -> None:
    """Тестирует вывод списка задач по категории."""
    task_manager.list_task(category='исследование')
    output = capsys.readouterr()
    expected_output = formatted_output([data_with_id[1], data_with_id[2]])
    assert output.out.strip() == expected_output
