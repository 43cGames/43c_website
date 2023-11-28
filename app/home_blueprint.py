from flask import Blueprint, render_template

from app.models import Example

home_blueprint = Blueprint("api", __name__, url_prefix="/home")

@home_blueprint.route('/')
def index():
    return render_template("layout.html")