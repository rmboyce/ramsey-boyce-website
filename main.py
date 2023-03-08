from flask import redirect, render_template, request

from daily_crossword import *
from javascript_demos import *
from projects import *
from route_config import app


# Force https
def force_https():
    # Redirect any non-https requests to https
    # Based largely on flask-sslify

    if not app.debug:
        app.config['SESSION_COOKIE_SECURE'] = True

    criteria = [
        app.debug,
        request.is_secure,
        request.headers.get('X-Forwarded-Proto', 'http') == 'https',
    ]

    if not any(criteria):
        if request.url.startswith('http://'):
            url = request.url.replace('http://', 'https://', 1)
            #code = 302
            code = 301
            r = redirect(url, code=code)
            return r

app.before_request(force_https)

#===================================
#=              Index              =
#===================================

@app.route('/index')
@app.route('/')
def index():
    return render_template('custom_page.html', title='About Me', page_content='pages/index.html')


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
