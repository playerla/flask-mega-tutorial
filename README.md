https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

Currently working on part 17-18-19

Python 3.8

# Testing mail

```sh
python -m smtpd -n -c DebuggingServer localhost:25
```

# Translating

```sh
pybabel extract -F babel.cfg -k _l -o messages.pot .
pybabel init -i messages.pot -d core/translations -l fr
# ... Edit messages.po
pybabel compile -d core/translations
# ... Modify python code
pybabel update -i messages.pot -d core/translations
```

# Switch Python version for Windows (livereload support 3.7)

```ps
$env:Path = "$env:LOCALAPPDATA\Programs\Python\Python37\;$env:Path"
```

# Fix elastic on WSL read only mode

https://stackoverflow.com/a/56143760

```bash
curl -XPUT -H "Content-Type: application/json" http://localhost:9200/_all/_settings -d '{"index.blocks.read_only_allow_delete": false}'
```

# VSCode Dev Environment Extension

- Python
- Gitlens
- Git Pull Requests
- Brower Preview
- Remote SSH/WSL
- SQlite
- SFTP
- reStructuredText

Not really usefull:
- Vagrant
- Visual Studio IntelliCode

# Hardened deployement on a VM

Deployed on /opt with user vagrant

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

# SMTP configuration

https://app.sendgrid.com/ with api key for local postfix relay

# Heroku configuration

heroku cli use git config to identify remote app
```bash
git remote add heroku git@heroku.com:microblog-flask-lopi.git
```

## Google cloud

```ps
$GOOGLE_CREDENTIALS= "GOOGLE_CREDENTIALS='"; gc .\google_credentials.json | % { $GOOGLE_CREDENTIALS += $_ }; $GOOGLE_CREDENTIALS+="'"
$GOOGLE_CREDENTIALS= ""; gc .\google_credentials.json | % { $GOOGLE_CREDENTIALS += $_ };
$env:EDITOR="code -w"
heroku config:edit GOOGLE_CREDENTIALS
heroku buildpacks:add --index 1 https://github.com/elishaterada/heroku-google-application-credentials-buildpack
```