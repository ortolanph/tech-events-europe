import logging
from logging import info

import yaml


class ConfigManager:
    _CONFIG_FILE = "config.yaml"
    _config = {}

    def __init__(self, environment):
        info(f"init:{environment}")
        with open(self._CONFIG_FILE, "r") as config_file:
            info("Reading config")
            self._config = yaml.safe_load(config_file)
            self._environment = environment
            config_file.close()

    def get_countries_data(self):
        logging.info("get_countries.data")
        return self._config['config'][self._environment]['countriesData']

    def get_template_file(self):
        logging.info("get_template_file")
        return self._config['config'][self._environment]['templateFile']
