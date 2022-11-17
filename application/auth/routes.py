from flask import Blueprint, render_template, redirect, url_for, request, flash
from application.models import User, db
from .forms import RegisterForm, LoginForm
from application import login_manager
from flask_login import login_user, logout_user, login_required, current_user

users = Blueprint('users', __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.username.data
        newuser = User(username=form.username.data,email=form.email.data)
        newuser.hash_pwd(form.password1.data)
        db.session.add(newuser)
        db.session.commit()
        flash('You are now registered')
        return redirect(url_for('base.index'))
    return render_template('auth/register.html', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('base.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            login_user(user)
            flash('Successfully logged in')
            return redirect(url_for('base.index'))
        else:
            flash('invalid credentials')
            return redirect(request.url)
    return render_template('auth/login.html', form=form)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('users.login'))
