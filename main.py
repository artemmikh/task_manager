from argparse import Namespace

from ui.configs import configure_argument_parser
from task_manager import TaskManager
from ui.command_dispatcher import CommandDispatcher


def main() -> None:
    """Основная функция для запуска программы."""
    arg_parser = configure_argument_parser()
    args: Namespace = arg_parser.parse_args()
    manager: TaskManager = TaskManager()
    dispatcher = CommandDispatcher(manager)
    dispatcher.dispatch(args)


if __name__ == '__main__':
    main()
