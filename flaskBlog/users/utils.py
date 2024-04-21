import os
import secrets
from PIL import Image
from flask import url_for
from flask_mail import Message
from flaskBlog import mail, app


def save_picture(from_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(from_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    out_size = (125, 125)
    i = Image.open(from_picture)
    i.thumbnail(out_size)
    i.save(picture_path)
    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password rest request',
                  sender='noreply@demo.com',
                  recipients=[user.email])

    msg.body = f''' To reset your password visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email
'''
    mail.send(msg)
