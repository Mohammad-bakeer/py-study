from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask import Flask, render_template
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    name = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
# csrf
app.secret_key = "xcv"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def login():
    form = MyForm()
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
