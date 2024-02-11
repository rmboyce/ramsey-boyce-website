from flask import Blueprint, abort, render_template, url_for
from markupsafe import Markup
from jinja2 import TemplateNotFound

from utils import title

#===================================
#=        Javascript Demos         =
#===================================

JS_MAP = {
    'chaos_game': ['chaos_game.js', 'Button.js', 'Checkbox.js', 'HScrollbar.js'],
    'element_words': ['element_words.js', 'HScrollbar.js', 'console.js'],
    'fractal_tree': ['fractal_tree.js', 'HScrollbar.js'],
    'orbit_simulator': ['orbit_sim.js', 'Button.js'],
    'particle_life': ['particle_life.js', 'HScrollbar.js', 'Button.js', 'Checkbox.js'],
    'voronoi_generator': ['voronoi_generator.js', 'Checkbox.js', 'Button.js']
}

def generate_js_markup(js_path, file_list):
    js = ''
    for f in file_list:
        js += f'''<script src="{url_for('static', filename=(f'js/{js_path}/{f}'))}" type="text/javascript"></script>\n'''
    return Markup(js)


javascript_demo_pages = Blueprint('javascript_demo_pages', __name__, template_folder='templates')

@javascript_demo_pages.route('/')
def javascript_demos():
    return render_template('custom_page.html', title='Javascript Demos', page_content='pages/javascript_demos.html')

@javascript_demo_pages.route('/<page>')
def show(page):
    try:
        j = generate_js_markup(page, JS_MAP[page])
        return render_template('js_demo_page.html', title=title(page), page_js=j, page_content=f'pages/javascript_demos/{page}.html')
    except TemplateNotFound:
        abort(404)
