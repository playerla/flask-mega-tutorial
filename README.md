https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

Currently working on part 14

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