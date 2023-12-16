from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField 
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

def f(x):
    l=[]
    if x != "☕️":
        l.append("✘")

    for i in range (5):
        c=""
        for j in range(i+1):
           c+=x
        l.append(c)
    return  l

        

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Cafe Location on Google Maps (URL)', validators=[URL(), DataRequired()])
    open_t = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close_t = StringField('Closning Time e.g. 5.30PM', validators=[DataRequired()])
    rating = SelectField('Coffe Rating', choices=f("☕️"), validators=[DataRequired()])
    wifi = SelectField('Wifi Strength Rating', choices=f("💪"), validators=[DataRequired()])
    power_socket = SelectField('Power Socket Availability', choices=f("🔌"), validators=[DataRequired()])
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET","POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('web/flask/14 15-12-2023/cafe-data.csv', "a", encoding='utf-8') as csv_file:
            data = "\n"+form.cafe.data+","+form.location.data+","+form.open_t.data+","+form.close_t.data+","+form.rating.data+","+form.wifi.data+","+form.power_socket.data
            csv_file.write(data)

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('web/flask/14 15-12-2023/cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
