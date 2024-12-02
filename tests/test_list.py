def test_empty_list_task(task_manager, capsys):
    task_manager.list_task()
    output = capsys.readouterr()
    assert output.out.strip() == 'Задачи не найдены'


def test_list_all_task(
        capsys, populate_db, data_with_id, task_manager, formatted_output):
    task_manager.list_task(all=True)
    output = capsys.readouterr()
    expected_output = formatted_output(data_with_id)
    assert output.out.strip() == expected_output


def test_list_task_by_category(
        capsys, populate_db, data_with_id, task_manager, formatted_output):
    task_manager.list_task(category='исследование')
    output = capsys.readouterr()
    expected_output = formatted_output([data_with_id[1], data_with_id[2]])
    assert output.out.strip() == expected_output
