import logging

from jinja2 import Template


class PageCreator:

    def __init__(self, page_template, country):
        logging.info(f"PageCreator::init::page_template:{page_template};country:{country}")
        self._page_template = page_template
        self._country = country

    def create_page(self, processed_events):
        logging.info(f"PageCreator::create_page::processed_events:{processed_events}")
        with open(self._page_template, "r") as page_template:
            logging.info("opening template")
            template = Template(
                page_template.read(),
                trim_blocks=True,
                lstrip_blocks=True)

        logging.info("rendering template")
        rendered_page = template.render(
            country=self._country.name,
            month_data=processed_events,
        )

        logging.info("saving rendered page")
        with open(f'pages/events_{self._country.code}.md', "w") as rendered_page_handler:
            rendered_page_handler.writelines(rendered_page)

    def __str__(self):
        return f'(PageCreator::page_template:{self._page_template}:country:{self._country})'
