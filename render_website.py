import json
import os
import argparse

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked

os.makedirs("pages", exist_ok=True)


def on_reload():

    parser = argparse.ArgumentParser(description='Запускает локальный сервер для онлайн библиотеки')
    parser.add_argument('--file_path', default="meta_data.json")
    args = parser.parse_args()

    with open(args.file_path, "r", encoding="utf-8") as my_file:
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