# line_statement_prefix and line_comment_prefix
from jinja2 import Template


class PageCreator:

    def __init__(self, page_template, country):
        self._page_template = page_template
        self._country = country

    def create_page(self, processed_events):
        with open(self._page_template, "r") as page_template:
            template = Template(page_template.read(), trim_blocks=True, lstrip_blocks=True)

        rendered_page = template.render(
            country=self._country.name,
            month_data=processed_events,
        )

        with open(f'pages/events_{self._country.code}.md', "w") as rendered_page_handler:
            rendered_page_handler.writelines(rendered_page)
