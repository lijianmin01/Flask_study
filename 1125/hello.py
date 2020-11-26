from flask_wtf import Form 
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask import Flask

app = Flask(__name__)
app.secret_key = "hard"

class NameForm(Form):
    name = StringField("What is your name?",validators=[Required()])
    submit = SubmitField('Submit')


