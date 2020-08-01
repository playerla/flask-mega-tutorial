### Base image
FROM python:3.8-alpine AS compile-image

RUN apk add build-base
RUN apk add linux-headers libffi-dev libressl-dev
# Compile grpcio for google-cloud-translate and cryptography on alpine Linux is time consuming, cache it
RUN pip install --user google-cloud-translate cryptography

### Create runtime image
FROM python:3.8-alpine AS base-image
RUN apk add libffi libressl
COPY --from=compile-image /root/.local /root/.local

WORKDIR /opt/microblog

### For db migration
RUN apk add git
RUN git clone https://github.com/vishnubob/wait-for-it
RUN git -c advice.detachedHead=false -C wait-for-it checkout c096cf
RUN chmod +x wait-for-it/wait-for-it.sh

### Deploy flask app
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY migrations migrations 
COPY microblog.py config.py .flaskenv .env ./

FROM base-image as runtime-image
COPY core core

ENTRYPOINT ["gunicorn"]
CMD [ "-b", ":5000", "--access-logfile", "-", "--error-logfile", "-", "microblog:app" ]

FROM base-image as dev-image

# For Development some addition
COPY watch.py watch.py
COPY playerla_livereload-2.6.1-py2.py3-none-any.whl ./
RUN pip install playerla_livereload-2.6.1-py2.py3-none-any.whl