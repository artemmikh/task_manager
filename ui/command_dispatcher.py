from argparse import Namespace

from services.task_manager import TaskManager


class CommandDispatcher:
    """Обрабатывает команды и вызывает соответствующие методы TaskManager."""

    def __init__(self, manager: TaskManager) -> None:
        self.manager = manager
        self.commands = {
            'add': self.manager.add_task,
            'remove': self.manager.remove_task,
            'list': self.manager.list_task,
            'search': self.manager.search_task,
            'edit': self.manager.edit_task
        }

    def dispatch(self, args: Namespace) -> None:
        """Вызывает метод TaskManager, соответствующий команде."""
        command = args.command
        manager_method = self.commands.get(command)
        if manager_method:
            manager_method(**vars(args))
        else:
            print(f'Команда {command} не поддерживается')
