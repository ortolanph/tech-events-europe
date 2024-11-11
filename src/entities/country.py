class Country:

    def __init__(self, name, code, flag_path):
        self.name = name
        self.code = code
        self.flag_path = flag_path

    def __str__(self):
        return f'(Country::name:{self.name}:code:{self.code}:flag_path:{self.flag_path})'