from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from sqlalchemy.exc import IntegrityError
import requests
import os
from dotenv import load_dotenv
load_dotenv()

#flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
####################################################################################
#db
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///C:/Users/Bakeer/OneDrive/Desktop/course 100D of Py/web/flask/16 28-12-2023(f)/top_movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#####################################################################################
url = "https://api.themoviedb.org/3/search/movie"
Auth= os.getenv("KEY")

headers = {
    "accept": "application/json",
    "Authorization": Auth
}
MOVIE_DB_IMAGE_URL="https://image.tmdb.org/t/p/w500"

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250))
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(250), nullable=False)


class RateForm(FlaskForm):
    rating = StringField('Your Review Out of 10 e.g. 7.5')
    review = StringField("Your Review")
    submit = SubmitField('Done')

class AddForm(FlaskForm):
    title = StringField("Movie Title")
    submit = SubmitField('Add Movie')



@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    
    #This line loops through all the movies
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route('/edit', methods=["GET","POST"])
def edit():
    form = RateForm()
    m_id = request.args.get('id')
    movie = Movie.query.get(m_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect("/")
    return render_template("edit.html", form=form, movie =movie)

@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddForm()
    
    if form.validate_on_submit():
        movie_title = form.title.data
        
        response = requests.get(url=url, params={"query": movie_title},headers=headers)
        data = response.json()["results"]
        return render_template("select.html", options=data)
      
    return render_template("add.html", form=form)

@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        n_url = url+f"/{movie_api_id}"
        response = requests.get(url=f"https://api.themoviedb.org/3/movie/{movie_api_id}", headers=headers)
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", id=new_movie.id))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

    