# Microblog

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

Full tutorial with minor adaptation done in some monthes

## Local Docker environment

### Test with downloding 1.0 (no build)

```sh
docker pull playerla/flaskmegaturorial:1.0
docker-compose -f docker-compose.yml up --no-build
docker-compose exec web flask shell
User.query.filter(User.username=='user').first().set_password(YOUR_PASSWORD_HERE)
db.session.commit()
exit()
```

I used Docker toolbox ("Native" Linux container on WSL 2 was still preview). See .env file for password and secret configuration.
Now using Docker for windows with WSL2 backend.

### Database migration utility

https://stackoverflow.com/a/44283611
https://gist.githubusercontent.com/skeep/10c30807e68c2dd7da820bd5cf7afe92/raw/c8c0a8f630f11def57a272eebeed8de630aaf806/docker-compose.yml
https://github.com/vishnubob/wait-for-it.git

### Removing database volume

Usefull on a permission denied, wrong former password stored on volume:
```ps
docker-compose stop db
docker-compose rm -v db
docker-compose up -d --build
# Run tool in a client container
docker run --network flask-mega-tuto_default -it --rm mysql mysql -hdb -uroot -p
# or attach in db container
docker-compose exec db mysql -hdb -p
```

### Reindexing all posts in search engine

Elastic volume has not been configured in this docker-compose file (not persistent)

```ps
docker-compose exec web flask index update
```

### Get mails

```ps
docker-compose logs -f smtp
```

## DEV Environment

- Windows 10, VirtualBox, WSL.
- VSCode
- Python 3.8

### SMTP configuration

https://app.sendgrid.com/ with api key for local postfix relay

#### Testing with local smtp

```sh
python -m smtpd -n -c DebuggingServer localhost:25
```

### Translating

```sh
pybabel extract -F babel.cfg -k _l -o messages.pot .
pybabel init -i messages.pot -d core/translations -l fr
# ... Edit messages.po
pybabel compile -d core/translations
```
```sh
# ... Modify python code and extract new pending translations
pybabel extract -F babel.cfg -k _l -o messages.pot .
pybabel update -i messages.pot -d core/translations
pybabel compile -d core/translations
```

### Switch Python version for Windows (livereload support 3.7)

```ps
$env:Path = "$env:LOCALAPPDATA\Programs\Python\Python37\;$env:Path"
```
Last version of livereload was broken I made a fix (a revert see [4fce73](https://github.com/playerla/python-livereload/commit/4fce737d541478c51424387d7432db0a0c0577ac))
Livereload work with `<script>` tag injection in `<head>`: 
```py
    return render_template_string("<html><head>world!<!-- script is injected here--></head><html>")
```

### Elasticsearch on WSL

Fix elastic on WSL read only mode : https://stackoverflow.com/a/56143760

```bash
curl -XPUT -H "Content-Type: application/json" http://localhost:9200/_all/_settings -d '{"index.blocks.read_only_allow_delete": false}'
```

### VSCode Extension

#### Used

- Python
- Jinja
- Gitlens
- Brower Preview
- Remote SSH/WSL
- SQlite
- SFTP
- Docker
- reStructuredText

#### Should take a look: 

- AREPL for python
- Better TOML
- TODO Highlight
- Bracket pair colorizer 2
- Toogle

## Hardened deployement tested on the Vagrant-VirtualBox (manual install of the application)

Deployed on /opt with user vagrant (SFTP extension is used here)

```bash
chown root:root /opt -R
find /opt -type d -exec setfacl -m "g:ubuntu:r-x" {} +
find /opt -type d -exec setfacl -m "g:vagrant:rwx" {} +
find /opt -type f -exec setfacl -m "g:vagrant:rwx" {} +
find /opt -type f -exec setfacl -m "g:ubuntu:r--" {} +
```
Check :
- user 'ubuntu' not in sudoers
- ubuntu permissions:executable+x, database+w and its folder +w
```bash
chown root:ubuntu /opt/microblog.db
chmod g+w /opt/microblog.db
chown root:ubuntu /opt/venv/bin/*
chmod g+x /opt/venv/bin/*
chown root:ubuntu /opt
chmod g+w /opt
```

## Heroku configuration

heroku cli use git config to identify remote app, set :
```bash
git remote add heroku git@heroku.com:microblog-flask-lopi.git
```
or on each command you will be asked for app-name : `heroku command -a app-name`

### Addons

- Redis
- SendGrid
- Postgres
- SearchBox Elasticsearch

### Heroku searchly : create index

http://www.searchly.com/docs/python

### Google cloud

Setup .\google-credentials.json content in $GOOGLE_CREDENTIALS

```ps
$GOOGLE_CREDENTIALS= ""; gc .\google-credentials.json | % { $GOOGLE_CREDENTIALS += $_ };
$env:EDITOR="code -w"
heroku config:edit GOOGLE_CREDENTIALS
heroku buildpacks:add --index 1 https://github.com/playerla/heroku-google-application-credentials-buildpack.git
```

NB: a .profile is executed at startup for manipulating the environment

## Reference and links

### Articles on python and docker
https://pythonspeed.com 
### Migration in real life
https://benchling.engineering/move-fast-and-migrate-things-how-we-automated-migrations-in-postgres-d60aba0fc3d4
### Introduction to Docker-compose
https://gabrieltanner.org/blog/docker-compose