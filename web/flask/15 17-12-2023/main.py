from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///C:/Users/Bakeer/OneDrive/Desktop/course 100D of Py/web/flask/15 17-12-2023/books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'



@app.route('/')
def home():
    all_books = Book.query.all()
    return render_template("index.html", books=all_books)

@app.route("/add", methods=["GET", "POST"])
def add():
    error_message = None

    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        rating = request.form["rating"]

        new_book = Book(title=title, author=author, rating=rating)

        try:
            db.session.add(new_book)
            db.session.commit()
            return redirect("/")
        except IntegrityError:
            db.session.rollback()
            error_message = "A book with the same title already exists."

    return render_template("add.html", error_message=error_message)

@app.route("/edit>", methods=["GET", "POST"])
def edit():
    if request.method=="POST":
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect("/")
    
    book_id = request.args.get('id')
    book = Book.query.get(book_id)
    return render_template("edit.html",book=book)

if __name__ == "__main__":
    app.run(debug=True)


"""
- Read A Particular Record By Query
    book = Book.query.filter_by(title="Harry Potter").first()

- Update A Particular Record By Query
    book_to_update = Book.query.filter_by(title="Harry Potter").first()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()  

- Update A Record By PRIMARY KEY
    book_id = 1
    book_to_update = Book.query.get(book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()  

- Delete A Particular Record By PRIMARY KEY 
    book_id = 1
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
*You can also delete by querying for a particular value e.g. by title or one of the other properties.

"""