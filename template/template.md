# {{country}} Events
{% for month in month_data %}

{% if month.events|length > 0 %}
## {{month.name}}

| Event Name | City  | Address  | Location | Start Date | End Date | Type |
|------------|-------|----------|----------|:----------:|:--------:|------|
{% for event in month.events %}
| [{{event.name}}]({{event.site}}) | {{event.city}} | {{event.address}} | {{event.location}} | {{event.start_date}}  | {{event.end_date}} | {{event.type}} |
{% endfor %}

[Back](../README.md)
{% endif %}
{% endfor %}


All event cost, accommodations, and transportation information are responsibilities of the organizers.
