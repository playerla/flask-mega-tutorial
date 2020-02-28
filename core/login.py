from flask_login import LoginManager
from core.main import app
from core.models import User

login = LoginManager(app)
login.login_view = 'login'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

