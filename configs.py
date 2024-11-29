import argparse


def configure_argument_parser():
    parser = argparse.ArgumentParser(description='Менеджер задач')
    subparsers = parser.add_subparsers(dest="command", required=True)
    add_parser = subparsers.add_parser('add', help='Добавление '
                                                   'задачи')
    add_parser.add_argument('-i', '--id', type=int, required=True,
                            help='ID задачи')
    add_parser.add_argument('-t', '--title', required=True,
                            help='Название задачи')
    return parser
