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