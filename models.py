from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
  db.app = app
  db.init_app(app)


class Pet(db.Model):
    __tablename__ = "pets"

    @classmethod
    def sort(cls):
        return cls.query.order_by(cls.available.desc(), cls.species, cls.name)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default="https://m.media-amazon.com/images/I/31dRVf4QrmL._AC_.jpg")
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)
