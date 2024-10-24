import datetime
import json
import logging

from src.entities.event import Event


def date_filter(event):
    today = datetime.date.today()

    current_year = today.year
    beginning_of_the_current_month = datetime.date(current_year, today.month, 1)
    last_day_of_year = datetime.date(current_year, 12, 31)

    return event.get_start_date() >= beginning_of_the_current_month and event.get_end_date() <= last_day_of_year


class EventRepository:
    _events = []

    def __init__(self, country_code):
        logging.info(f"EventRepository::init:{country_code}")
        self._events = []
        event_file = f'events/events_{country_code}.json'

        with open(event_file, 'r') as event_file_handler:
            events = json.loads(event_file_handler.read())

            for event in events:
                self._events.append(Event(
                    event['name'],
                    event['site'],
                    event['city'],
                    event['address'],
                    event['location'],
                    datetime.date.fromisoformat(event['start_date']),
                    datetime.date.fromisoformat(event['end_date']),
                    event['type']))

            event_file_handler.close()

    def get_events(self):
        logging.info("EventRepository::get_events")
        return self._events

    def get_upcoming_events(self):
        logging.info("EventRepository::get_upcoming_events")
        return list(filter(date_filter, self._events))
