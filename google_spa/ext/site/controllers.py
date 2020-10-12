from google_spa.ext.db import db
from google_spa.ext.db.models import Articles


def insert_article_in_db(name, body):
    article = Articles(name=name, body=body)
    db.session.add(article)
    db.session.commit()
    

