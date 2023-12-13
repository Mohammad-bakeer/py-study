from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask import Flask, render_template
from wtforms.validators import DataRequired, Email, Length


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[
                             DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
# csrf
app.secret_key = "xcv"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    form.validate_on_submit()
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
