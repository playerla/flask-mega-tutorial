from core.main import app
from core import routes
from core import login
from core.models import db, User, Post, Message, Notification, Task

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message,
        'Notification': Notification, 'Task': Task}

@app.cli.group()
def index():
    """Search index commands."""
    pass

@index.command()
def update():
    """Reindex Posts."""
    Post.reindex()