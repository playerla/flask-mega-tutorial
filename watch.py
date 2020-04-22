from livereload import Server
import importlib
from traceback import format_exc
from time import sleep

while True:
    microblog = importlib.util.find_spec("microblog")
    microblog = importlib.util.module_from_spec(microblog)
    try:
        from microblog import app
        app.debug = True
        server = Server(app.wsgi_app)
        server.serve(port=5000, host="0.0.0.0")
    except Exception as e:
        print(f'Ignoring [{e.__class__.__name__}] {e}', flush=True)
        print(format_exc(), flush=True)
        print('Will reload in 3 second', flush=True)
        sleep(3)
        continue