from flask import Blueprint, abort, render_template
from jinja2 import TemplateNotFound

from route_config import app
from utils import title

#===================================
#=            Projects             =
#===================================

@app.route('/projects')
def projects():
    return render_template('custom_page.html', title='My Projects', page_content='pages/projects.html')

project_pages = Blueprint('project_pages', __name__, template_folder='templates')

@project_pages.route('/projects/<page>')
def show(page):
    try:
        return render_template('custom_page.html', title=title(page), page_content=f'pages/projects/{page}.html')
    except TemplateNotFound:
        abort(404)

app.register_blueprint(project_pages)
