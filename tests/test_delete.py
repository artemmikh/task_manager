from main import TaskManager


def test_delete_task_by_id(temp_db, monkeypatch, populate_db, data_with_id):
    monkeypatch.setattr(TaskManager, 'db', temp_db)
    manager = TaskManager()
    count_tasks = len(manager.tasks)

    id_to_delete = data_with_id['id']
    manager.remove_task(id=id_to_delete)
    assert len(manager.tasks) == count_tasks - 1
    for task in manager.tasks:
        assert task.id == id_to_delete
        break


def test_delete_task_by_category(
        temp_db, monkeypatch, populate_db, data_with_id):
    monkeypatch.setattr(TaskManager, 'db', temp_db)
    manager = TaskManager()

    count_tasks = len(manager.tasks)
    category_to_delete = data_with_id['category']
    manager.remove_task(category=category_to_delete)
    assert len(manager.tasks) == count_tasks - 1
    for task in manager.tasks:
        assert task.category == category_to_delete
