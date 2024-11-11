import csv
from logging import info

from src.entities.country import Country


def filter_by_country_code(country: Country, country_code):
    return country.code == country_code


class CountryRepository:
    _country_data = []
    _FIELD_NAMES = ["Country", "Code", "Flag"]

    def __init__(self, countries_file):
        info(f"CountryRepository::init:country_file:{countries_file}")
        with open(countries_file, "r") as country_file_handler:
            info(f"Opening data file")
            country_file_csv_data = csv.DictReader(
                country_file_handler,
                fieldnames=self._FIELD_NAMES,
                delimiter=",",
            )

            info(f"Skipping header")
            next(country_file_csv_data)

            for data in country_file_csv_data:
                self._country_data.append(Country(
                    data[self._FIELD_NAMES[0]],
                    data[self._FIELD_NAMES[1]],
                    data[self._FIELD_NAMES[2]])
                )

            country_file_handler.close()

    def get_country_list(self):
        info(f"CountryRepository::get_country_list")
        return self._country_data

    def get_country_by_code(self, country_code):
        info(f"CountryRepository::get_country_by_code::country_code:{country_code}")
        result = list(filter(lambda c: filter_by_country_code(c, country_code), self._country_data))
        return result[0] if len(result) > 0 else None

    def __str__(self):
        return f'(CountryRepository::country_data:{self._country_data})'
