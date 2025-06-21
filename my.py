import os
from time import sleep

from dotenv import load_dotenv
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import LoginManager, UserMixin, login_required, login_user
from markupsafe import Markup
from mysecrets import LINKS
from werkzeug.security import check_password_hash  # , generate_password_hash

from route_config import app

load_dotenv()

app.secret_key = os.environ.get("SECRET_KEY")
login_manager = LoginManager()
login_manager.login_view = "my_pages.login"
login_manager.init_app(app)


class User(UserMixin):
    """
    Basic user class.
    """

    def __init__(self, user_id) -> None:
        super().__init__()
        self.user_id = user_id

    def get_id(self):
        return self.user_id


USER = User("user")


@login_manager.user_loader
def load_user(user_id):
    if user_id == "user":
        return USER


my_pages = Blueprint("my_pages", __name__, template_folder="templates")


@my_pages.route("/login")
def login():
    return render_template("login.html", title="Login")


@my_pages.route("/api/login", methods=["POST"])
def login_post():
    sleep(1)
    PASSWORD = request.form.get("password")
    REMEMBER = bool(request.form.get("remember"))

    if not check_password_hash(os.environ.get("PASSWORD"), PASSWORD):
        flash("Please check your login details and try again.")
        return redirect(url_for("my_pages.login"))

    login_user(USER, remember=REMEMBER)
    return redirect(url_for("my_pages.show"))


def generate_links():
    html = ""
    for link in LINKS:
        html += f'<li>\n<a href="{link}" target="_blank">{link}</a>\n</li>\n'
    return Markup(html)


@my_pages.route("/links")
@login_required
def show():
    links = generate_links()
    return render_template("links.html", title="Links", links=links)
