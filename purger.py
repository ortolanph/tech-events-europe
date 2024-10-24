# Purge all previous events end_date < today
import logging
from argparse import ArgumentParser

logging.basicConfig(
    format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s',
    level=logging.INFO)


def main(environment):
    pass


if __name__ == '__main__':
    logging.info("Purger")
    parser = ArgumentParser(
        prog="purger",
        description="Generates the event page for a single country",
        add_help=True
    )
    parser.add_argument(
        "--environment", "-env",
        help="Choose the environment",
        type=str,
        choices=["test", "prod"],
        default="prod",
        required=False
    )
    main("test")
