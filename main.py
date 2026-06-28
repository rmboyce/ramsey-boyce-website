import os
from flask import render_template, request, redirect
from werkzeug import Response

# from daily_crossword import daily_crossword_pages
from misc import misc_pages
from game import game_pages

# from my import my_pages
from projects import project_pages
from route_config import app
from visualizations import visualization_pages

# ===================================
# =              Index              =
# ===================================


@app.before_request
def force_https() -> Response | None:
    # ProxyFix handles request.is_secure safely behind your proxy
    if not app.debug and not request.is_secure:
        if request.url.startswith("http://"):
            url = request.url.replace("http://", "https://", 1)
            return redirect(url, code=301)


@app.before_request
def clear_trailing() -> Response | None:
    request_path = request.path
    if request_path != "/" and request_path.endswith("/"):
        query = request.query_string.decode("utf-8")
        target_url = f"{request_path[:-1]}?{query}" if query else request_path[:-1]
        return redirect(target_url, code=301)


@app.route("/index")
@app.route("/")
def index():
    return render_template(
        "custom_page.html", title="Ramsey Boyce", page_content="pages/index.html"
    )


# Error page
@app.errorhandler(404)
def page_not_found(_):
    # Set the 404 status explicitly
    return render_template("404.html"), 404


# Register blueprints for pages
# app.register_blueprint(daily_crossword_pages, url_prefix="/daily_crossword")
# app.register_blueprint(my_pages, url_prefix='/my')
app.register_blueprint(project_pages, url_prefix="/projects")
app.register_blueprint(visualization_pages, url_prefix="/projects/visualizations")
app.register_blueprint(misc_pages, url_prefix="/misc")
app.register_blueprint(game_pages, url_prefix="/game")


# Only runs on local machine
if os.environ.get("GAE_ENV") != "standard":
    print(app.url_map)
    app.run(debug=True)
