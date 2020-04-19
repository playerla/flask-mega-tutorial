from livereload import Server
from microblog import app

app.debug = True
server = Server(app.wsgi_app)
server.serve(port=5000, host="0.0.0.0")