import argparse


def configure_argument_parser(available_modes):
    parser = argparse.ArgumentParser(description='Менеджер задач')
    parser.add_argument(
        'mode',
        choices=available_modes,
        help='Режимы работы менеджера'
    )
    return parser
