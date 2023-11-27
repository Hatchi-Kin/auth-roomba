from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import json


db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    ics_url = db.Column(db.String(100))
    checkpoint = db.Column(db.Text)  

    def get_name(self):
        return self.username
    
    def set_ics_url(self, ics_url):
        self.ics_url = ics_url
        db.session.commit()

    def get_ics_url(self):
        return self.ics_url

    def set_checkpoint(self, checkpoint):
        self.checkpoint = json.dumps(checkpoint)
        db.session.commit()

    def get_checkpoint(self):
        return json.loads(self.checkpoint) if self.checkpoint else None



def load_user(user_id):
    return User.query.get(int(user_id))
