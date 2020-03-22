from livereload import Server
from microblog import app

app.debug = True
server = Server(app.wsgi_app)
server.serve()