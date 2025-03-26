import logging

from src.entities.country import Country
from src.entities.month_event import MonthEvent
from src.page.page_creator import PageCreator
from src.repository.event_repository import EventRepository


def filter_month_by_id(month_data, month_id):
    return month_data.get_id() == month_id


def date_sorter(event):
    return event.get_start_date()


def filter_events_by_month(event, month):
    return event.get_start_date().month == month


class Processor:
    def process(self):
        pass


class SingleCountryProcessor(Processor):
    _events_by_month = [
        MonthEvent(1, "January"),
        MonthEvent(2, "February"),
        MonthEvent(3, "March"),
        MonthEvent(4, "April"),
        MonthEvent(5, "May"),
        MonthEvent(6, "June"),
        MonthEvent(7, "July"),
        MonthEvent(8, "August"),
        MonthEvent(9, "September"),
        MonthEvent(10, "October"),
        MonthEvent(11, "November"),
        MonthEvent(12, "December"),
    ]

    def __init__(self, country: Country, event_repository: EventRepository, template_file):
        logging.info(f"SinglePageProcessor::init::country:{country};event_repository:{event_repository};template_file:{template_file}")
        self._country = country
        self._event_repository = event_repository
        self._template_file = template_file
        self._page_creator = PageCreator(template_file, country)

    def process(self):
        logging.info(f"SinglePageProcessor::process")
        logging.info(f"processing events for country {self._country.code}")
        events = self._event_repository.get_upcoming_events()
        events.sort(key=date_sorter, reverse=False)
        first_month = events[0].get_start_date().month

        arranged_events = []

        for month in range(first_month, 13):
            logging.info(f"events for month:{month}")
            current_month = \
                list(filter(lambda month_data: filter_month_by_id(month_data, month), self._events_by_month))[0]

            selected_events = list(filter(lambda event: filter_events_by_month(event, month), events))
            current_month.clear_events()
            current_month.add_events(selected_events)

            arranged_events.append(current_month.to_dict())

        self._page_creator.create_page(arranged_events)


class AllCountriesProcessor(Processor):

    def __init__(self, processors: []):
        logging.info(f"AllCountriesProcessor::init::processors:{processors}")
        self._processors = processors

    def process(self):
        logging.info(f"AllCountriesProcessor::processing all countries")
        for country_processor in self._processors:
            country_processor.process()
