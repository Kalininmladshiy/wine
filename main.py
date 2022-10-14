import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from utils import get_noun_form, get_age, get_drinks_by_category
from pathlib import Path


if __name__ == '__main__':
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    
    template = env.get_template('template.html')
    
    parser = argparse.ArgumentParser(
        description='Сайт винодельни'
    )
    parser.add_argument(
        "--path_to_file",
        help="Файл с товарными категориями",
        default=Path.cwd() / 'wine.xlsx',
    )
    args = parser.parse_args()    
    
    winery_age=get_age()
    drinks_by_category = get_drinks_by_category(args.path_to_file)
    rendered_page = template.render(
        winery_age=winery_age,
        drinks_by_category=drinks_by_category,
        noun_form=get_noun_form(winery_age),
    )
    
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
