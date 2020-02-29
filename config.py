import os
basedir = os.path.abspath(os.path.dirname(__file__))

config = {
    'SECRET_KEY': os.environ.get('SECRET_KEY') or 'you-will-never-guess',
    'SQLALCHEMY_DATABASE_URI':'sqlite:///' + os.path.join(basedir, 'microblog.db'),
    'SQLALCHEMY_TRACK_MODIFICATIONS':False,
    'MAIL_SERVER':'localhost',
    'ADMINS':['your-email@example.com'],
    'POSTS_PER_PAGE':3,
    'LANGUAGES':['en', 'fr'],
    'BABEL_TRANSLATION_DIRECTORIES':'./translations/'
}