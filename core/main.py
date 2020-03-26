from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from config import config
from flask_moment import Moment
from flask_babel import Babel
from core.models import db, User
from core.auth.email import init_auth
from core.search import CoreSearch

app = Flask(__name__)
app.config.update(config)
app.elasticsearch = CoreSearch(app)

db.init_app(app)
migrate = Migrate(app, db)
# Sign up is disable so populate with some users
with app.app_context():
    try:
        if User.query.filter_by(username='admin').count() == 0:
            u = User(
                username='admin',
                email='administrateur@microblog-flask-lopi.com',
                password_hash="pbkdf2:sha256:150000$2XacMguc$bfc3752840f5e99164824768a597fcd582b59676ef154b29d70c5aaf874ce2ed"
            )
            u2 = User(
                username='user',
                email='user@microblog-flask-lopi.com',
                password_hash="pbkdf2:sha256:150000$g6t07GxN$7b9b24a4a6d6b6f26a15ffa6e9e2ee333dbbfc7e0464fca0e45ccaf818bde3d4"
            )
            db.session.bulk_save_objects([u,u2])
            db.session.commit()
            print(f'{u} and {u2} created')
    except:
        print("Can't create default users")
Bootstrap(app)
init_auth(app)
moment = Moment(app)
babel = Babel(app)
