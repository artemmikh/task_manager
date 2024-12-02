import argparse


def configure_argument_parser():
    parser = argparse.ArgumentParser(description='Менеджер задач')
    subparsers = parser.add_subparsers(
        dest='command', required=True)
    list_parser = subparsers.add_parser(
        'list', help='Посмотреть список задач')
    delete_parser = subparsers.add_parser('remove', help='Удаление задачи')
    delete_group = delete_parser.add_mutually_exclusive_group(required=True)
    delete_group.add_argument(
        '--id',
        type=int,
        help='ID задачи для удаления')
    delete_group.add_argument(
        '--category',
        help='Категория задач для удаления')
    search_parser = subparsers.add_parser('search', help='Поиск задачи')
    search_group = search_parser.add_mutually_exclusive_group(required=True)
    search_group.add_argument(
        '-kw',
        '--keyword',
        help='ключевое слово для поиска задачи')
    search_group.add_argument(
        '-c',
        '--category',
        help='категория задачи для поиска')
    search_group.add_argument(
        '-s',
        '--status',
        help='статус задачи для поиска')
    add_parser = subparsers.add_parser(
        'add', help='Добавление задачи')
    add_parser.add_argument(
        '-t', '--title', required=True, help='название')
    add_parser.add_argument(
        '-d',
        '--description',
        help='описание',
        required=True)
    add_parser.add_argument(
        '-c',
        '--category',
        help='категория',
        required=True)
    add_parser.add_argument(
        '-dt',
        '--due_date',
        help='срок выполнения',
        required=True)
    add_parser.add_argument(
        '-p',
        '--priority',
        help='приоритет',
        required=True,
        choices=['низкий', 'средний', 'высокий'])
    add_parser.add_argument(
        '-s',
        '--status',
        help='статус',
        required=True,
        choices=['выполнена', 'не выполнена'])
    return parser
