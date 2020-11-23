from flask import render_template,Flask
from flask_wtf import Form, FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required, DataRequired


# class NameForm(Form):
#     name = StringField('What is your name?', validators=[Required()])
#     submit = SubmitField('Submit')

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


app = Flask(__name__)
app.config["SECRET_KEY"] = '79537d00f4834892986f09a100aa1edf'

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    return render_template('index.html', form=form, name=name)

if __name__ == '__main__':
    app.run(debug=True)