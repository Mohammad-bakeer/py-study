from flask import Flask, render_template
import requests

response = requests.get(url="https://api.npoint.io/ecc1074ed577e3b62c3c")
response.raise_for_status()
data = response.json()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", data=data)


@app.route("/<path:page>")
def static_page(page):
    return render_template(page)


@app.route("/post/<int:num>")
def post(num):
    return render_template("post.html", data=data, num=num-1)


if __name__ == "__main__":
    app.run(debug=True)
