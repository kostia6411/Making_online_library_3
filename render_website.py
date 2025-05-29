import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked
import os


os.makedirs("pages", exist_ok=True)


def on_reload():
    with open("meta_data.json", "r", encoding="utf-8") as my_file:
        books = my_file.read()

    books = json.loads(books)

    dozen_books = list(chunked(books, 10))
    
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )

    template = env.get_template('template.html')

    for number, page in enumerate(dozen_books, 1):

        rows_books =  list(chunked(page, 2))

        rendered_page = template.render(
            rows_books = rows_books,
            pages_number = len(dozen_books),
            current_number = number
        )

        with open(f'pages/index{number}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)

on_reload()

server = Server()

server.watch('template.html', on_reload)

server.serve(root='.')