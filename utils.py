from flask import redirect, request, Response

from route_config import app


def title(page: str) -> str:
    return page.replace("_", " ").title()


def force_https() -> Response | None:
    # Redirect any non-https requests to https
    # Based largely on flask-sslify

    if not app.debug:
        app.config["SESSION_COOKIE_SECURE"] = True

    criteria = [
        app.debug,
        request.is_secure,
        request.headers.get("X-Forwarded-Proto", "http") == "https",
    ]

    if not any(criteria):
        if request.url.startswith("http://"):
            url = request.url.replace("http://", "https://", 1)
            return redirect(url, code=301)


def clear_trailing() -> Response | None:
    # Clear trailing /s from urls
    request_path = request.path
    if request_path != "/" and request_path.endswith("/"):
        return redirect(request_path[:-1], code=301)
