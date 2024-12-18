from flask import render_template

from daily_crossword import daily_crossword_pages
from visualizations import visualization_pages
#from my import my_pages
from projects import project_pages
from route_config import app
from utils import clear_trailing, force_https

#===================================
#=              Index              =
#===================================

app.before_request(force_https)
app.before_request(clear_trailing)


@app.route('/index')
@app.route('/')
def index():
    return render_template('custom_page.html', title='Ramsey Boyce', page_content='pages/index.html')

# Error page
@app.errorhandler(404)
def page_not_found(_):
    # Set the 404 status explicitly
    return render_template('404.html'), 404


# Register blueprints for pages
app.register_blueprint(daily_crossword_pages, url_prefix='/daily_crossword')
#app.register_blueprint(my_pages, url_prefix='/my')
app.register_blueprint(project_pages, url_prefix='/projects')
app.register_blueprint(visualization_pages, url_prefix='/projects/visualizations')


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
