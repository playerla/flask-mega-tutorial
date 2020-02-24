from flask_login import LoginManager
from core.main import app
from core.models import User

login = LoginManager(app)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

