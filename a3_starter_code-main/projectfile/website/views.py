from flask import Blueprint, render_template, request, redirect, url_for
from .models import MusicShow
from . import db

mainbp = Blueprint('main', __name__)


@mainbp.route('/')
def index():
    music_shows = db.session.scalars(db.select(MusicShow)).all()
    return render_template('index.html', music_shows=music_shows)

@mainbp.route('/search')
def search():
    if request.args['search'] and request.args['search'] != "":
        print(request.args['search'])
        query = "%" + request.args['search'] + "%"
        music_shows = db.session.scalars(db.select(MusicShow).where(MusicShow.name.like(query)))
        return render_template('index.html', music_shows=music_shows)
    else:
        return redirect(url_for('main.index'))