from flask import Blueprint, render_template
from markupsafe import Markup

# ===================================
# =         Serpent Fusion          =
# ===================================

serpent_fusion_pages = Blueprint(
    "serpent_fusion_pages", __name__, template_folder="templates"
)


@serpent_fusion_pages.route("/")
def serpent_fusion():
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
        page_content="pages/serpent_fusion.html",
        squeeze=False,
    )
