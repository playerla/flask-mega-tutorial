from core.main import app
from core import routes
from core import login
from core.models import db, User, Post, Message, Notification, Task
from core.auth.email import send_email

def test_email(recipients):
    send_email('[Microblog] Reset Your Password',
            sender=app.config['ADMINS'][0],
            recipients=recipients,
            text_body="test_mail",
            html_body="<p>test_mail</p>")

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message,
        'Notification': Notification, 'Task': Task, 'test_email': test_email}

@app.cli.group()
def index():
    """Search index commands."""
    pass

@index.command()
def update():
    """Reindex Posts."""
    Post.reindex()