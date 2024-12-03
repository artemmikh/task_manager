from typing import List, Dict
import pytest

from task_manager import TaskManager


@pytest.mark.parametrize(
    'search_param, indexes',
    [
        ({'keyword': 'ключевым'}, [0, 1]),
        ({'category': 'исследование'}, [1, 2]),
        ({'status': 'выполнена'}, [0, 2])
    ]
)
def test_search_task(
        search_param: Dict[str, str], indexes: List[int],
        capsys: pytest.CaptureFixture,
        populate_db: None, task_manager: TaskManager,
        data_with_id: List[Dict[str, str]],
        formatted_output: callable) -> None:
    task_manager.search_task(**search_param)
    output = capsys.readouterr()
    expected_output = formatted_output([data_with_id[i] for i in indexes])
    assert output.out.strip() == expected_output
