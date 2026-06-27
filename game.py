from flask import Blueprint, render_template
from markupsafe import Markup

# ===================================
# =         Serpent Fusion          =
# ===================================

game_pages = Blueprint("game_pages", __name__, template_folder="templates")


@game_pages.route("/")
def game():
    HEAD = Markup("""
    <style>
        canvas {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 75dvh;
            overflow: hidden;
            z-index: 0;
            background: black;
            display: block;
            outline: none;
            -webkit-tap-highlight-color: transparent;
        }
    </style>
    """)
    return render_template(
        "custom_page.html",
        title="Serpent Fusion",
        head_html=HEAD,
        page_content="pages/game.html",
        squeeze=False,
    )
