web: flask db upgrade; gunicorn microblog:app
worker: rq worker microblog-tasks -u $REDIS_URL