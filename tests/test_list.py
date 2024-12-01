def test_empty_list_task(task_manager, capsys):
    task_manager.list_task()
    output = capsys.readouterr()
    assert output.out.strip() == 'Задачи не найдены'


def test_list_task(capsys, populate_db, data_with_id, task_manager):
    task_manager.list_task()
    output = capsys.readouterr()
    expected_output = (
        f'id – {data_with_id["id"]}, '
        f'название – {data_with_id["title"]}, '
        f'описание – {data_with_id["description"]}, '
        f'категория – {data_with_id["category"]}, '
        f'срок выполнения – {data_with_id["due_date"]}, '
        f'приоритет – {data_with_id["priority"]}, '
        f'статус – {data_with_id["status"]}'
    )
    assert output.out.strip() == expected_output
