from wtforms import Form,StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length

class LoginForm(Form):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])