import argparse


def configure_argument_parser():
    def add_list_arguments(parser):
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument(
            '-a',
            '--all',
            action='store_true',
            help='список всех задач')
        group.add_argument(
            '-c',
            '--category',
            help='список задач по категории')

    def add_task_arguments(parser):
        parser.add_argument('-t', '--title', required=True, help='название')
        parser.add_argument('-d', '--description', required=True,
                            help='описание')
        parser.add_argument('-c', '--category', required=True,
                            help='категория')
        parser.add_argument('-dt', '--due_date', required=True,
                            help='срок выполнения')
        parser.add_argument(
            '-p', '--priority', required=True, help='приоритет',
            choices=['низкий', 'средний', 'высокий']
        )
        parser.add_argument(
            '-s', '--status', required=True, help='статус',
            choices=['выполнена', 'не выполнена']
        )

    def add_search_arguments(parser):
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('-kw', '--keyword',
                           help='ключевое слово для поиска задачи')
        group.add_argument('-c', '--category',
                           help='категория задачи для поиска')
        group.add_argument('-s', '--status', help='статус задачи для поиска')

    def add_remove_arguments(parser):
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('--id', type=int, help='ID задачи для удаления')
        group.add_argument('--category', help='Категория задач для удаления')

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

    return parser
