import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked


def on_reload():
    with open("meta_data.json", "r", encoding="utf-8") as my_file:
        books = my_file.read()

    books = json.loads(books)

    rows_books =  list(chunked(books, 2))

    # for books in rows_books:
    #     for book in books:
    #         print(book)
    
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        rows_books = rows_books
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

on_reload()

server = Server()

server.watch('template.html', on_reload)

server.serve(root='.')