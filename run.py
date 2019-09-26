from app import create_app, db
from app.auth.models import User

if __name__ == '__main__':
    #flask_app = create_app('dev')
    flask_app = create_app('prod')
    with flask_app.app_context():  # tells flask to use current application context
        db.create_all() # create database tables
        if not User.query.filter_by(user_name = 'harry').first():
            User.create_user(user = 'harry',
                             email = 'harry@potter.com',
                             password = 'secret')

    flask_app.run()