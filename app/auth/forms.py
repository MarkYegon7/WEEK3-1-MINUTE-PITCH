from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import InputRequired,Email,EqualTo
from wtforms import ValidationError
from ..models import User




class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[InputRequired()])
    password = PasswordField('Password',validators=[InputRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')