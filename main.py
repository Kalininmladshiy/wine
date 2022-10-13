from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from utils import noun_form, get_age, get_drinks_by_category


if __name__ == '__main__':
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    
    template = env.get_template('template.html')
    
    winery_age=get_age()
    drinks_by_category = get_drinks_by_category()
    rendered_page = template.render(
        winery_age=winery_age,
        drinks_by_category=drinks_by_category,
        noun_form=noun_form(winery_age),
    )
    
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
