from core.main import app
from core import routes
from core.models import db, User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}