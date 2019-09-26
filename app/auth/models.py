from datetime import datetime
from app import db, bcrypt          # from app/__init__.py
from app import login_manager
from flask_login import UserMixin

class User(UserMixin, db.Model): # inherits from UserMixin
    __tablename__ = 'users'

    # Table columns
    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(20))
    user_email = db.Column(db.String(60), unique= True, index=True)
    user_password = db.Column(db.String(60))
    registration_date = db.Column(db.DateTime, default = datetime.now)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.user_password, password)

    # Class methods belong to the class but are not associated wth any class instance
    # Can be called on the class rather than the instance
    # Classmethods can be treated as alternative constructors (since python only allows one __init__ method per class)
    @classmethod
    def create_user(cls, user, email, password):    # takes in cls rather than self
        user = cls(user_name = user,
                   user_email = email,
                   user_password = bcrypt.generate_password_hash(password).decode('utf-8')
                   )

        db.session.add(user)
        db.session.commit()
        return user

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))