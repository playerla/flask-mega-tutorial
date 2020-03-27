import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(basedir, '.env'))

config = {
    'SECRET_KEY': os.environ.get('SECRET_KEY') or '86g746g63737g8d7438s6f',
    'SQLALCHEMY_DATABASE_URI': os.environ.get('DATABASE_URL') or ('sqlite:///' + os.path.join(basedir, 'microblog.db')),
    'SQLALCHEMY_TRACK_MODIFICATIONS':False,
    'MAIL_SERVER':'localhost',
    'ADMINS':['administrateur@microblog-flask-lopi.com'],
    'POSTS_PER_PAGE':3,
    'LANGUAGES':['en', 'fr'],
    'BABEL_TRANSLATION_DIRECTORIES':'./translations/',
    'ELASTICSEARCH_URL': os.environ.get('ELASTICSEARCH_URL') or "localhost:9200"
}