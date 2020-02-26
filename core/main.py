from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from core.models import db
from config import config
import logging
from logging.handlers import SMTPHandler

app = Flask(__name__)
app.config.update(config)

db.init_app(app)
migrate = Migrate(app, db)
Bootstrap(app)

if not app.debug:
    if app.config['MAIL_SERVER']:
        print('Configured to send mail')
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure')
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)