from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from core.models import db
from config import config

app = Flask(__name__)
app.config.update(config)

db.init_app(app)
with app.app_context():
    db.drop_all()
    db.create_all()
migrate = Migrate(app, db)
Bootstrap(app)