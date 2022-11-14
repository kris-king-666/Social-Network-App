from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Email
from application.models import User


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired('You must enter a username')])
    email = EmailField('Email Address', validators=[DataRequired('You must enter an email address'), Email()])
    password1 = PasswordField('Set Password', validators=[DataRequired('You must enter a password')])
    password2 = PasswordField('Repeat Password',
                              validators=[DataRequired('Passwords must match'), EqualTo('password1')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError('Username is already registered.  Please pick a different one')


class LoginForm(FlaskForm):
    email = EmailField('Email Address', validators=[DataRequired('You must enter an email address'), Email()])
    password = PasswordField('Password', validators=[DataRequired('You must enter a password')])
    submit = SubmitField('Login')

    def validate_username(self, username):
        if not User.query.filter_by(username=self.username.data).first():
            raise ValidationError('Username is not recognised')
