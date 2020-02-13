from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class ServiceForm(FlaskForm):

    name = StringField('Service name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    status = BooleanField('Is running')
    admin = BooleanField('Only for admin')
    port = IntegerField('Port', validators=[DataRequired()])
    github = StringField('Github address', validators=[DataRequired()])
    submit = SubmitField('Add')