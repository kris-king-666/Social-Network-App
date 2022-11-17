from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Email
from flask_wtf.file import FileField, FileAllowed
from application.models import User


class ProfileUpdateForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired('You must enter a username')])
    email = EmailField('Email Address', validators=[DataRequired('You must enter an email address'), Email()])
    profilepic = FileField('Image', validators=[FileAllowed(['jpg', 'jpeg', 'webp', 'png'])])
    aboutme = TextAreaField()
    submit = SubmitField('Update Profile')
