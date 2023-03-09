from flask import render_template

import daily_crossword
import javascript_demos
import projects
from route_config import app
from utils import force_https


#===================================
#=              Index              =
#===================================

app.before_request(force_https)

@app.route('/index')
@app.route('/')
def index():
    return render_template('custom_page.html', title='About Me', page_content='pages/index.html')

# Error page
@app.errorhandler(404)
def page_not_found(_):
    # Set the 404 status explicitly
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
