import pytest


def format_expected_output(tasks):
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


@pytest.mark.parametrize(
    'search_param, indexes',
    [
        ({'keyword': 'ключевым'}, [0, 1]),
        ({'category': 'исследование'}, [1, 2]),
        ({'status': 'выполнена'}, [0, 2])
    ]
)
def test_search_task(search_param, indexes, capsys, populate_db, task_manager,
                     data_with_id):
    task_manager.search_task(**search_param)
    output = capsys.readouterr()
    expected_output = format_expected_output(data_with_id[i] for i in indexes)
    assert output.out.strip() == expected_output
