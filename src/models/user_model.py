from app import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200))
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    last_login = db.Date(db.String(200))
    password = db.Column(db.String(200))

    def __repr__(self):
        return "<User %r>" % self.username
