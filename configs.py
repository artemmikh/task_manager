import argparse


def configure_argument_parser():
    parser = argparse.ArgumentParser(description='Менеджер задач')
    subparsers = parser.add_subparsers(
        dest='command', required=True)
    list_parser = subparsers.add_parser(
        'list', help='Посмотреть список задач')
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
