# Single Country Processor
from argparse import ArgumentParser

from src.config.config_manager import ConfigManager
from src.processor.processors import SingleCountryProcessor
from src.repository.country_repository import CountryRepository
from src.repository.event_repository import EventRepository


def main(country_code):
    config = ConfigManager()
    country_repository = CountryRepository(config.get_countries_data())
    country_data = country_repository.get_country_by_code(country_code)

    if not country_data is None:
        event_repository = EventRepository(f'data/events_{country_code}.json')
        country_processor = SingleCountryProcessor(country_data, event_repository, config.get_template_file())

        country_processor.process()
    else:
        print(f'Country not found {country_code}')


if __name__ == '__main__':
    parser = ArgumentParser(
        prog="single_country",
        description="Generates the event page for a single country",
        add_help=True
    )
    parser.add_argument(
        "--country_code", "-cc",
        type=str,
        help="The country code",
        required=True
    )
    arguments = parser.parse_args()

    main(arguments.country_code)
