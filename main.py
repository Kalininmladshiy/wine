from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from utils import noun_form, get_years, get_drinks_data


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

winery_age=get_years()
drinks_data = get_drinks_data()
rendered_page = template.render(
    winery_age=winery_age,
    drinks_data=drinks_data,
    noun_form=noun_form(winery_age),
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
