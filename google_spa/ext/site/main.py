from flask import Blueprint
from .controllers import insert_article_in_db

bp = Blueprint("spa", __name__)

@bp.route("/")
def index():
    insert_article_in_db('Python', 'Python para iniciantes')
    return 'Oi tô on'