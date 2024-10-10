import logging


def config_logging(process_name: str) -> None:
    logging.basicConfig(
        filename=f'../logs/{process_name}.log', # logs folder path
        encoding='utf-8',
        filemode='w',
        format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.ERROR
    )
    return
