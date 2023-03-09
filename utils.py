from flask import redirect, request

from route_config import app


def title(page):
    return page.replace('_', ' ').title()

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