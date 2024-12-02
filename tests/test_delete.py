import json


def test_delete_task_by_id(populate_db, temp_db, task_manager, data_with_id):
    count_tasks = len(task_manager.tasks)
    id_to_delete = data_with_id[0]['id']
    task_manager.remove_task(id=id_to_delete)
    assert len(task_manager.tasks) == count_tasks - 1
    for task in task_manager.tasks:
        assert task.id != id_to_delete
    with open(temp_db, 'r', encoding='utf-8') as file:
        tasks = json.load(file)
        for task in tasks:
            assert task['id'] != id_to_delete


def test_delete_task_by_category(populate_db, temp_db, task_manager,
                                 data_with_id):
    category_to_delete = data_with_id[0]['category']
    task_manager.remove_task(category=category_to_delete)
    for task in task_manager.tasks:
        assert task.category != category_to_delete
    with open(temp_db, 'r', encoding='utf-8') as file:
        tasks = json.load(file)
        for task in tasks:
            assert task['id'] != category_to_delete
