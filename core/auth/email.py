from flask_mail import Message
from flask import render_template, current_app
from threading import Thread
from flask_mail import Mail
from logging import ERROR
from logging.handlers import SMTPHandler

mail = Mail()

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(current_app._get_current_object(), msg)).start()

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset Your Password',
               sender=current_app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))

def init_auth(app):
    mail.init_app(app)
    if not app.debug:
        if app.config['MAIL_SERVER']:
            print('Configured to send mail')
            mail_handler = SMTPHandler(
                mailhost=(app.config['MAIL_SERVER']),
                fromaddr='no-reply@' + app.config['MAIL_SERVER'],
                toaddrs=app.config['ADMINS'], subject='Microblog Failure')
            mail_handler.setLevel(ERROR)
            app.logger.addHandler(mail_handler)