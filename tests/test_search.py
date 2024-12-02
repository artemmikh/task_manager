import pytest


@pytest.mark.parametrize(
    'search_param, indexes',
    [
        ({'keyword': 'ключевым'}, [0, 1]),
        ({'category': 'исследование'}, [1, 2]),
        ({'status': 'выполнена'}, [0, 2])
    ]
)
def test_search_task(search_param, indexes, capsys, populate_db, task_manager,
                     data_with_id, formatted_output):
    task_manager.search_task(**search_param)
    output = capsys.readouterr()
    expected_output = formatted_output(data_with_id[i] for i in indexes)
    assert output.out.strip() == expected_output
