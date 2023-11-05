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
        query = "%" + request.args['search'] + "%"
        music_shows = db.session.scalars(db.select(MusicShow).where(MusicShow.name.like(query)))
        return render_template('index.html', music_shows=music_shows)
    else:
        return redirect(url_for('main.index'))
    
@mainbp.route('/filter_location')
def filter_location():
    if request.args['filter_location'] and request.args['filter_location'] != "":
        query = "%" + request.args['filter_location'] + "%"
        music_shows = db.session.scalars(db.select(MusicShow).where(MusicShow.location.like(query)))
        return render_template('index.html', music_shows=music_shows)
    else:
        return redirect(url_for('main.index'))
    
@mainbp.route('/filter_artists')
def filter_artists():
    if request.args['filter_artists'] and request.args['filter_artists'] != "":
        query = "%" + request.args['filter_artists'] + "%"
        music_shows = db.session.scalars(db.select(MusicShow).where(MusicShow.artists.like(query)))
        return render_template('index.html', music_shows=music_shows)
    else:
        return redirect(url_for('main.index'))
    
@mainbp.route('/filter_genre')
def filter_genre():
    if request.args['filter_genre'] and request.args['filter_genre'] != "":
        query = "%" + request.args['filter_genre'] + "%"
        music_shows = db.session.scalars(db.select(MusicShow).where(MusicShow.genre.like(query)))
        return render_template('index.html', music_shows=music_shows)
    else:
        return redirect(url_for('main.index'))