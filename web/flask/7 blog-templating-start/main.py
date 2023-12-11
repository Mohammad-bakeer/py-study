from flask import Flask, render_template
import requests

response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
content = response.json()


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", blog_t=content)


@app.route('/blog/<num>')
def post(num):
    num = int(num) - 1
    return render_template("post.html", blog_t=content, num=int(num))


if __name__ == "__main__":
    app.run(debug=True)
