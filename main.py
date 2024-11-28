from configs import configure_argument_parser


def add_task():
    pass


def delete_task():
    pass


MODE_TO_FUNCTION = {
    'add-task': add_task,
    'delete-task': delete_task,
}


def main():
    arg_parser = configure_argument_parser(MODE_TO_FUNCTION.keys())
    args = arg_parser.parse_args()
    parser_mode = args.mode
    MODE_TO_FUNCTION[parser_mode]()


if __name__ == '__main__':
    main()
