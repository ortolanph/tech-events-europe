import yaml

class ConfigManager:

    _CONFIG_FILE = "config.yaml"
    _config = {}

    def __init__(self):
        with open(self._CONFIG_FILE, "r") as config_file:
            self._config = yaml.safe_load(config_file)

    def get_countries_data(self):
        return self._config['config']['countriesData']

    def get_template_file(self):
        return self._config['config']['templateFile']
