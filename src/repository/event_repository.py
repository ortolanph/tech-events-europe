import datetime
import json

from src.entities.event import Event


def date_filter(event):
    today = datetime.date.today()

    current_year = today.year
    beginning_of_the_current_month = datetime.date(current_year, today.month, 1)
    last_day_of_year = datetime.date(current_year, 12, 31)

    return event.start_date >= beginning_of_the_current_month and event.end_date <= last_day_of_year


class EventRepository:
    _events = []

    def __init__(self, event_file):
        with open(event_file, 'r') as event_file_handler:
            events = json.loads(event_file_handler.read())

            for event in events:
                self._events.append(Event(
                    event['event_name'],
                    event['event_site'],
                    event['city'],
                    event['address'],
                    event['location'],
                    datetime.date.fromisoformat(event['start_date']),
                    datetime.date.fromisoformat(event['end_date']),
                    event['type']))

    def get_events(self):
        return self._events

    def get_upcoming_events(self):
        return list(filter(date_filter, self._events))
