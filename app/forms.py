from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from flask_wtf import FlaskForm
from app.models import User

class LoginForm(FlaskForm):
  username = StringField("Username", validators=[DataRequired()])
  password = PasswordField("Password", validators=[DataRequired()])
  remember_me = BooleanField("Remember Me")
  submit = SubmitField("Sign in")

class CreateAccountForm(FlaskForm):
  username = StringField("Username", validators=[DataRequired()])
  password = PasswordField("Password", validators=[DataRequired()])
  age = IntegerField("Age", validators=[DataRequired()])
  submit = SubmitField("Sign up")

class RegistrationForm(FlaskForm):
  username = StringField("Username", validators=[DataRequired()])
  email = StringField("Email", validators=[DataRequired(), Email()])
  password = PasswordField("Password", validators=[DataRequired()])
  password2 = PasswordField("Repeat Password", validators=[DataRequired(), EqualTo("password")])
  submit = SubmitField("Register")

  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user is not None:
      raise ValidationError("Please use a different username")

  def validate_email(self, email):
    user = User.query.filter_by(username=email.data).first()
    if user is not None:
      raise ValidationError("Please use a different email address")

class EditProfileForm(FlaskForm):
  username = StringField("Username", validators=[DataRequired()])
  about_me = TextAreaField("About me", validators=[Length(min=0, max=140)])
  submit = SubmitField("Submit")