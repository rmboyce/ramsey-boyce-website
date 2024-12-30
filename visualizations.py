from flask import Blueprint, abort, render_template, url_for
from markupsafe import Markup

from utils import title

# ===================================
# =         Visualizations          =
# ===================================

JS_MAP = {
    "chaos_game": ["chaos_game.js", "Button.js", "Checkbox.js", "HScrollbar.js"],
    "element_words": ["element_words.js", "HScrollbar.js", "console.js"],
    "fractal_tree": ["fractal_tree.js", "HScrollbar.js"],
    "orbit_simulator": ["orbit_sim.js", "Button.js"],
    "particle_life": ["particle_life.js", "HScrollbar.js", "Button.js", "Checkbox.js"],
    "voronoi_generator": ["voronoi_generator.js", "Checkbox.js", "Button.js"],
}


def generate_js_markup(js_path, file_list):
    js = ""
    for file in file_list:
        js += f"""<script src="{url_for('static', filename=(f'js/{js_path}/{file}'))}" type="text/javascript"></script>\n"""
    return Markup(js)


visualization_pages = Blueprint(
    "visualization_pages", __name__, template_folder="templates"
)


@visualization_pages.route("/")
def visualizations():
    return render_template(
        "custom_page.html",
        title="Visualizations",
        page_content="pages/visualizations.html",
    )


@visualization_pages.route("/<page>")
def show(page: str):
    try:
        JS = generate_js_markup(page, JS_MAP[page])
        return render_template(
            "js_demo_page.html",
            title=title(page),
            page_js=JS,
            page_content=f"pages/visualizations/{page}.html",
        )
    except:
        abort(404)
