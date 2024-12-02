def test_empty_list_task(task_manager, capsys):
    task_manager.list_task()
    output = capsys.readouterr()
    assert output.out.strip() == 'Задачи не найдены'


def test_list_task(capsys, populate_db, data_with_id, task_manager):
    task_manager.list_task()
    output = capsys.readouterr()
    expected_output = "\n".join([
        (
            f'id – {task["id"]}, '
            f'название – {task["title"]}, '
            f'описание – {task["description"]}, '
            f'категория – {task["category"]}, '
            f'срок выполнения – {task["due_date"]}, '
            f'приоритет – {task["priority"]}, '
            f'статус – {task["status"]}'
        )
        for task in data_with_id
    ])
    assert output.out.strip() == expected_output
