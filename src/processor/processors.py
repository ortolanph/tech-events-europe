from src.entities.country import Country
from src.repository.event_repository import EventRepository


class Processor:
    def process(self):
        pass


class SingleCountryProcessor(Processor):

    def __init__(self, country: Country, event_repository: EventRepository, template_file):
        self._country = country
        self._event_repository = event_repository
        self._template_file = template_file

    def process(self):
        print(f"processing country {self._country.name}")


class AllCountriesProcessor(Processor):

    def __init__(self, processors: [Processor]):
        self._processors = processors

    def process(self):
        for country_processor in self._processors:
            country_processor.process()
