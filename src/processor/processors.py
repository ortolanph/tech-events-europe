from src.entities.country import Country
from src.repository.event_repository import EventRepository


class Processor:
    def process(self):
        pass


class SingleCountryProcessor(Processor):

    _MONTHS = [
        {
            "month_number": 1,
            "month_name": "January"
        },
        {
            "month_number": 2,
            "month_name": "February"
        },
        {
            "month_number": 3,
            "month_name": "March"
        },
        {
            "month_number": 4,
            "month_name": "April"
        },
        {
            "month_number": 5,
            "month_name": "May"
        },
        {
            "month_number": 6,
            "month_name": "June"
        },
        {
            "month_number": 7,
            "month_name": "July"
        },
        {
            "month_number": 8,
            "month_name": "August"
        },
        {
            "month_number": 9,
            "month_name": "September"
        },
        {
            "month_number": 10,
            "month_name": "October"
        },
        {
            "month_number": 11,
            "month_name": "November"
        },
        {
            "month_number": 12,
            "month_name": "December"
        }
    ]

    def __init__(self, country: Country, event_repository: EventRepository, template_file):
        self._country = country
        self._event_repository = event_repository
        self._template_file = template_file

    def process(self):
        for event in self._event_repository.get_upcoming_events():
            pass


class AllCountriesProcessor(Processor):

    def __init__(self, processors: [Processor]):
        self._processors = processors

    def process(self):
        for country_processor in self._processors:
            country_processor.process()
