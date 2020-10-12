from google_spa.ext.db import db

class Articles(db.Model):
    __tablename__ = "articles"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode)
    body = db.Column("body", db.Unicode)