import json
from jinja2 import Environment, FileSystemLoader, select_autoescape

with open("meta_data.json", "r", encoding="utf-8") as my_file:
    meta_data_json = my_file.read()

meta_data = json.loads(meta_data_json)

# print(meta_data)


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html'])
)
template = env.get_template('template.html')

rendered_page = template.render(
    meta_data = meta_data
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

