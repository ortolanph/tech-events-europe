# Single Country Processor
import logging
from logging import info
from argparse import ArgumentParser



from src.config.config_manager import ConfigManager
from src.processor.processors import SingleCountryProcessor
from src.repository.country_repository import CountryRepository
from src.repository.event_repository import EventRepository

logging.basicConfig(
    format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s',
    level=logging.INFO)


def main(country_code, environment):
    info(f"main:{country_code}:{environment}")
    config = ConfigManager(environment)
    country_repository = CountryRepository(config.get_countries_data())
    country_data = country_repository.get_country_by_code(country_code)

    if not country_data is None:
        event_repository = EventRepository(country_code)
        country_processor = SingleCountryProcessor(country_data, event_repository, config.get_template_file())

        country_processor.process()
    else:
        print(f'Country not found {country_code}')


if __name__ == '__main__':
    info("Single Country Processor")
    parser = ArgumentParser(
        prog="single_country",
        description="Generates the event page for a single country",
        add_help=True
    )
    parser.add_argument(
        "--country_code", "-cc",
        help="The country code",
        type=str,
        required=True
    )
    parser.add_argument(
        "--environment", "-env",
        help="Choose the environment",
        type=str,
        choices=["test", "prod"],
        default="prod",
        required=False
    )
    arguments = parser.parse_args()

    main(arguments.country_code, arguments.environment)
