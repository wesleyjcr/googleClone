from flask import Blueprint, jsonify, request
from .controllers import insert_article_in_db, select_all_items

bp = Blueprint("spa", __name__)


@bp.route("/insert")
def insert():
    content = request.json
    name = content["name"]
    body = content["body"]
    insert_article_in_db(name, body)
    return "Sucessful"


@bp.route("/search")
def search():
    data = request.args.get("name")
    articles = select_all_items(data)
    response = []
    for article in articles:
        response.append({"name": article.name, "body": article.body})

    return jsonify(response)
