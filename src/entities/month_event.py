def to_event_dict(event):
    return event.to_dict()


class MonthEvent:

    def __init__(self, month_id, month):
        self._id = month_id
        self._month = month
        self._events = []

    def add_events(self, events):
        self._events.extend(events)

    def clear_events(self):
        self._events = []

    def get_id(self):
        return self._id

    def to_dict(self):
        return {
            "id": self._id,
            "name": self._month,
            "events": list(map(to_event_dict, self._events))
        }

    def __str__(self):
        return f'(MonthEvent::id:{self._month}:month:{self._month}:events:{self._events})'
