import os
config = {
    'SECRET_KEY': os.environ.get('SECRET_KEY') or 'you-will-never-guess',
    'SQLALCHEMY_DATABASE_URI':'sqlite:///:memory:',
    'SQLALCHEMY_TRACK_MODIFICATIONS':False
}