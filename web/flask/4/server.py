from flask import Flask, render_template
from datetime import datetime
import requests
app = Flask(__name__)


@app.route('/')
def home():

    today = datetime.now()
    year = today.year
    return render_template('index.html', y=year)


@app.route('/guess/<name>')
def guess(name):
    parameters = {"name": name}
    response_1 = requests.get(
        url="https://api.genderize.io", params=parameters)
    response_1.raise_for_status()
    response_2 = requests.get(url="https://api.agify.io", params=parameters)
    response_2.raise_for_status()
    return f'<h1>Hi {name.title()}</h1>'\
        f'<p>i think you are {response_2.json()["age"]} years old<br>and that you are a {response_1.json()["gender"]}</p>'


if __name__ == "__main__":
    app.run(debug=True)
