from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.auth.models import User

# Custom validators
def email_exists(form, field):
    email = User.query.filter_by(user_email = field.data).first()
    if email:
        raise ValidationError('Email already exists')

# Create a registration form, which is a class of FlaskForm
class RegistrationForm(FlaskForm):

    name = StringField("Enter your Name", validators=[DataRequired(), Length(3,15, message='Must be 3 to 15 characters')])
    email = StringField("Enter your Email", validators=[DataRequired(), Email(), email_exists])
    password = PasswordField("Password", validators=[DataRequired(), Length(5), EqualTo('confirm', message = 'passwords must match')])
    confirm = PasswordField("Confirm Password", validators=[DataRequired()])

    submit = SubmitField("Register")

# Login form
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    stay_loggedin = BooleanField('stay logged-in')
    submit = SubmitField('Login')