from flask import Blueprint, render_template, request, redirect, url_for
from .models import Comment, MusicShow
from .forms import MusicShowForm, CommentForm
from . import db
import os
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user

# name - first argument is the blueprint name 
# import name - second argument - helps identify the root url for it 
destbp = Blueprint('music_show', __name__, url_prefix='/music_shows')

@destbp.route('/<id>')
def show(id):
    music_show = db.session.scalar(db.select(MusicShow).where(MusicShow.id==id))
    cform = CommentForm()
    return render_template('music_shows/show.html', music_show=music_show, form=cform)

@destbp.route('/create', methods = ['GET', 'POST'])
@login_required
def create():
    print('Method type: ', request.method)
    form = MusicShowForm()
    if form.validate_on_submit():
        db_file_path = check_upload_file(form)
        music_show = MusicShow(name=form.name.data, description=form.description.data, image=db_file_path, 
                               genre=form.genre.data, status=form.status.data, start_date=form.start_date.data, 
                               end_date=form.end_date.data, artists=form.artists.data, location=form.location.data, 
                               num_tickets_avaliable=form.num_tickets_avaliable.data, promocode=form.promocode.data)
        db.session.add(music_show)
        db.session.commit()
        print('Successfully created new music show', 'success')
        return redirect(url_for('music_show.create'))
    return render_template('music_shows/create.html', form=form)

@destbp.route('/<id>/comment', methods = ['GET', 'POST'])
@login_required
def comment(id):
  #here the form is created  form = CommentForm()
  form = CommentForm()
  
  music_show = db.session.scalar(db.select(MusicShow).where(MusicShow.id==id))

  if form.validate_on_submit():	#this is true only in case of POST method
      comment = Comment(text=form.text.data, music_show=music_show, user=current_user)
      db.session.add(comment)
      db.session.commit()
      print('Your comment has been added', 'success') 
  # notice the signature of url_for
  return redirect(url_for('music_show.show', id=id))

def check_upload_file(form):
  #get file data from form  
  fp = form.image.data
  filename = fp.filename
  #get the current path of the module file… store image file relative to this path  
  BASE_PATH = os.path.dirname(__file__)
  #upload file location – directory of this file/static/image
  upload_path = os.path.join(BASE_PATH, 'static/image', secure_filename(filename))
  #store relative path in DB as image location in HTML is relative
  db_upload_path = '/static/image/' + secure_filename(filename)
  #save the file and return the db upload path
  fp.save(upload_path)
  return db_upload_path