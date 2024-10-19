import csv

from src.entities.country import Country


def filter_by_country_code(country: Country, country_code):
    return country.code == country_code


class CountryRepository:
    _country_data = []
    _FIELD_NAMES = ["Country", "Code", "Flag"]

    def __init__(self, countries_file):
        with open(countries_file, "r") as country_file_handler:
            country_file_csv_data = csv.DictReader(
                country_file_handler,
                fieldnames=self._FIELD_NAMES,
                delimiter=","
            )

            for data in country_file_csv_data:
                self._country_data.append(Country(data['Country'], data['Code'], data['Flag']))

    def get_country_list(self):
        return self._country_data

    def get_country_by_code(self, country_code):
        result = list(filter(lambda c : filter_by_country_code(c, country_code), self._country_data))
        return result[0] if len(result) > 0 else None
