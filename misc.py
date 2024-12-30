from flask import Blueprint, abort, render_template

from utils import title

# ===================================
# =              Blog               =
# ===================================

misc_pages = Blueprint("misc_pages", __name__, template_folder="templates")


@misc_pages.route("/")
def projects():
    return render_template(
        "custom_page.html",
        title="Miscellaneous",
        page_content="pages/misc.html",
    )


@misc_pages.route("/<page>")
def show(page: str):
    try:
        return render_template(
            "custom_page.html",
            title=title(page),
            page_content=f"pages/misc/{page}.html",
        )
    except:
        abort(404)
