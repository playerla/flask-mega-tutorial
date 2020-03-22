from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from config import config
from flask_moment import Moment
from flask_babel import Babel
from core.models import db
from core.auth.email import init_auth

app = Flask(__name__)
app.config.update(config)

db.init_app(app)
migrate = Migrate(app, db)
Bootstrap(app)
init_auth(app)
moment = Moment(app)
babel = Babel(app)
