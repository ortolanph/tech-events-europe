from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"


class Event:

    def __init__(self, name, site,
                 city, address, location, start_date, end_date, type):
        self._name = name
        self._site = site
        self._city = city
        self._address = address
        self._location = location
        self._start_date = start_date
        self._end_date = end_date
        self._type = type

    def get_start_date(self):
        return self._start_date

    def get_end_date(self):
        return self._end_date

    def to_dict(self):
        return {
            "name": self._name,
            "site": self._site,
            "city": self._city,
            "address": self._address,
            "location": self._location,
            "start_date": datetime.strftime(self._start_date, DATE_FORMAT),
            "end_date": datetime.strftime(self._end_date, DATE_FORMAT),
            "type": self._type
        }
