def test_search_task_by_keyword(capsys, populate_db, task_manager, temp_db,
                                data_with_id):
    task_to_search = data_with_id[0]
    task_manager.search_task(keyword=task_to_search["title"])
    output = capsys.readouterr()
    expected_output = (
        f'id – {task_to_search["id"]}, '
        f'название – {task_to_search["title"]}, '
        f'описание – {task_to_search["description"]}, '
        f'категория – {task_to_search["category"]}, '
        f'срок выполнения – {task_to_search["due_date"]}, '
        f'приоритет – {task_to_search["priority"]}, '
        f'статус – {task_to_search["status"]}'
    )
    assert output.out.strip() == expected_output
