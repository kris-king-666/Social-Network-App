from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed
from datetime import datetime


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired('You must enter a title')])
    subtitle = StringField('Subtitle', validators=[DataRequired('You must enter a subtitle')])
    date = DateField('Date Posted', default=datetime.utcnow())
    pic = FileField('Image', validators=[FileAllowed(['jpg', 'jpeg', 'webp', 'png'])])
    body = TextAreaField('')
    submit = SubmitField('Post')