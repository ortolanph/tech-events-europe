import logging
from argparse import ArgumentParser

from src.config.config_manager import ConfigManager
from src.processor.processors import AllCountriesProcessor, SingleCountryProcessor, Processor
from src.repository.country_repository import CountryRepository
from src.repository.event_repository import EventRepository

logging.basicConfig(
    format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s',
    level=logging.INFO)

def main(environment):
    logging.info(f"main:{environment}")
    config = ConfigManager(environment)
    country_repository = CountryRepository(config.get_countries_data())
    countries = country_repository.get_country_list()

    processors = []

    for country in countries:
        event_repository = EventRepository(country.code)
        processor = SingleCountryProcessor(country, event_repository, config.get_template_file())
        processors.append(processor)

    all_country_processor = AllCountriesProcessor(processors)
    all_country_processor.process()


if __name__ == '__main__':
    logging.info("All Countries Processor")
    parser = ArgumentParser(
        prog="single_country",
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
    arguments = parser.parse_args()

    main(arguments.environment)
