import argparse


def add_edit_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '--id', type=int, required=True,
        help='ID задачи для редактирования'
    )
    parser.add_argument('-t', '--title', help='Новое название задачи')
    parser.add_argument('-d', '--description', help='Новое описание задачи')
    parser.add_argument('-c', '--category', help='Новая категория задачи')
    parser.add_argument(
        '-dt', '--due_date', help='Новый срок выполнения задачи'
    )
    parser.add_argument(
        '-p', '--priority', help='Новый приоритет задачи',
        choices=['низкий', 'средний', 'высокий']
    )
    parser.add_argument(
        '-s', '--status', help='Новый статус задачи',
        choices=['выполнена', 'не выполнена']
    )


def add_list_arguments(parser: argparse.ArgumentParser) -> None:
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '-a',
        '--all',
        action='store_true',
        help='Список всех задач'
    )
    group.add_argument(
        '-c',
        '--category',
        help='Список задач по категории'
    )


def add_task_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument('-t', '--title', required=True, help='Название')
    parser.add_argument('-d', '--description', required=True, help='Описание')
    parser.add_argument('-c', '--category', required=True, help='Категория')
    parser.add_argument('-dt', '--due_date', required=True,
                        help='Срок выполнения')
    parser.add_argument(
        '-p', '--priority', required=True, help='Приоритет',
        choices=['низкий', 'средний', 'высокий']
    )
    parser.add_argument(
        '-s', '--status', required=True, help='Статус',
        choices=['выполнена', 'не выполнена']
    )


def add_search_arguments(parser: argparse.ArgumentParser) -> None:
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-kw', '--keyword',
                       help='Ключевое слово для поиска задачи')
    group.add_argument('-c', '--category', help='Категория задачи для поиска')
    group.add_argument('-s', '--status', help='Статус задачи для поиска')


def add_remove_arguments(parser: argparse.ArgumentParser) -> None:
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--id', type=int, help='ID задачи для удаления')
    group.add_argument('--category', help='Категория задач для удаления')


def configure_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Менеджер задач')
    subparsers = parser.add_subparsers(dest='command', required=True)
    list_parser = subparsers.add_parser('list', help='Посмотреть список задач')
    add_list_arguments(list_parser)
    add_parser = subparsers.add_parser('add', help='Добавление задачи')
    add_task_arguments(add_parser)
    search_parser = subparsers.add_parser('search', help='Поиск задачи')
    add_search_arguments(search_parser)
    remove_parser = subparsers.add_parser('remove', help='Удаление задачи')
    add_remove_arguments(remove_parser)
    edit_parser = subparsers.add_parser('edit', help='Изменение задачи')
    add_edit_arguments(edit_parser)
    return parser
