from flask import Blueprint, flash, render_template, request, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from .forms import LoginForm, RegisterForm
from flask_login import login_user, login_required, logout_user
from . import db

# create a blueprint
authbp = Blueprint('auth', __name__)


@authbp.route('/register', methods=['GET', 'POST'])
def register():
    register = RegisterForm()
    if (register.validate_on_submit() == True):

        pwd = register.password.data
        email = register.email_id.data
        uname = register.user_name.data

        user = db.session.scalar(db.select(User).where(User.name == uname))

        if user:
            flash('Username already exists, please try another')
            return redirect(url_for('auth.register'))

        pwd_hash = generate_password_hash(pwd)

        new_user = User(name=uname, password_hash=pwd_hash, emailid=email)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('main.index'))
    else:
        return render_template('user.html', form=register, heading='Register')


# this is a hint for a login function
@authbp.route('/login', methods=['GET', 'POST'])
def login():

    login_form = LoginForm()
    error = None
    if (login_form.validate_on_submit() == True):
        user_name = login_form.user_name.data
        password = login_form.password.data
        user = db.session.scalar(db.select(User).where(User.name == user_name))
        if user is None:
            error = 'Incorrect credentials supplied'
        # takes the hash and password
        elif not check_password_hash(user.password_hash, password):
            error = 'Incorrect credentials supplied'
        if error is None:
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash(error)
    return render_template('user.html', form=login_form, heading='Login')


@authbp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
