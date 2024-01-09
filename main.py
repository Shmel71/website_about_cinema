from flask import Flask, render_template, g
import sqlite3 as sq
import DBase

app = Flask(__name__)
app.config['DATABASE'] = "static/db/films.db"
app.secret_key = "qwer1234"


def connect_db():
    connect = sq.connect(app.config['DATABASE'])
    connect.row_factory = sq.Row
    return connect


@app.route("/films/<int:film_id>")
def film(film_id):
    db = DBase.ConnectToDb(connect_check())
    film = db.get_film(film_id)
    if film:
        return render_template("film.html", menu=navigation, film=film)
    else:
        return render_template("404.html", menu=navigation)


def connect_check():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


navigation = [
    {"link": "/", "name": "Главная страница"},
    {"link": "/films", "name": "Фильмотека"},
    {"link": "/info", "name": "Обо мне"}
]


@app.route("/")
def index():
    return render_template("index.html", menu=navigation)


@app.route("/films")
def films():
    db = DBase.ConnectToDb(connect_check())
    return render_template("films.html", menu=navigation, films=db.get_film_content())


@app.route("/info")
def info():
    return render_template("info.html", menu=navigation)


@app.teardown_appcontext
def connect_close(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == "__main__":
    app.run()
