from flask_login import LoginManager
from core.main import app
from core.models import User
from flask_babel import lazy_gettext as _l

login = LoginManager(app)
login.login_view = 'auth.login'
login.login_message = _l('Please log in to access this page.')

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

