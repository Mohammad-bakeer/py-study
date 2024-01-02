from flask import Flask, render_template, request, jsonify
import requests

response = requests.get(url="https://api.npoint.io/ecc1074ed577e3b62c3c")
response.raise_for_status()
data = response.json()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", data=data)


"""
@app.route("/<path:page>")
def static_page(page):
    return render_template(page)
"""


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg=True)
    return render_template("contact.html", msg=False)


@app.route("/post/<int:num>")
def post(num):
    return render_template("post.html", data=data, num=num-1)


"""
@app.route("/form-entry", methods=["POST"])
def receive_data():
    data = request.form
    print(data["name"])
    print(data["email"])
    print(data["phone"])
    print(data["message"])
    return "<h1>Successfully sent your message</h1>"
"""

if __name__ == "__main__":
    app.run(debug=True)
