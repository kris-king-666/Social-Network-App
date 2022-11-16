from flask import Blueprint, render_template, redirect, url_for, flash
from application.models import User, db
from .forms import ProfileUpdateForm

profile = Blueprint('profile', __name__)


@profile.route('/viewprofile/<int:id>')
def viewprofile(id):
    user = User.query.filter_by(id=id).first()
    return render_template('profile/profile.html', user=user)


@profile.route('/updateprofile/<int:id>', methods=['GET', 'POST'])
def updateprofile(id):
    form = ProfileUpdateForm()
    user = User.query.filter_by(id=id).first()
    if form.validate_on_submit():
        email = form.email.data
        aboutme = form.aboutme.data
        user.email = form.email.data
        user.username = form.username.data
        user.aboutme = form.aboutme.data
        db.session.commit()
        flash('Profile successfully updated')
        return redirect(url_for('profile.viewprofile',id=id))
    form.email.data = user.email
    form.username.data = user.username
    form.profilepic.data = user.profilepic
    form.aboutme.data = user.aboutme
    return render_template('profile/updateprofile.html', form=form)
