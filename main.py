from argparse import Namespace

from repository.task_repository import TaskRepository
from ui.configs import configure_argument_parser
from services.task_manager import TaskManager
from ui.command_dispatcher import CommandDispatcher


def main() -> None:
    """Основная функция для запуска программы."""
    arg_parser = configure_argument_parser()
    args: Namespace = arg_parser.parse_args()
    repository = TaskRepository()
    manager = TaskManager(repository)
    dispatcher = CommandDispatcher(manager)
    dispatcher.dispatch(args)


if __name__ == '__main__':
    main()
