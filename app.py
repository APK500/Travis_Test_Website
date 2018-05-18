from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(12), unique=True, nullable=True)

    def __repr__(self):
        return '<Movie %r>' % self.movie_title



# create route that renders index.html template
@app.route("/")
def index():
    return "I am an index page"

@app.route("/send", methods=["GET","POST"])
def send_data():
    if request.method == "POST":
        movie_title = request.form["movie_title"]
        imdb_id = request.form["imdb_id"]
        return redirect("/", code=302)

    return render_template("form.html")


if __name__ == "__main__":
    app.run()
