class Event:

    def __init__(self, country_code, event_name, event_site,
                 city, address, start_date, end_date, type):
        self.country_code = country_code
        self.event_name = event_name
        self.event_site = event_site
        self.city = city
        self.address = address
        self.start_date = start_date
        self.end_date = end_date
        self.type = type
