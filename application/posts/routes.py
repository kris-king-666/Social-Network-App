import os.path
import secrets
from PIL import Image
from flask import Blueprint, render_template, flash, current_app, redirect, url_for
from flask_login import current_user

from .forms import PostForm
from application.models import Post
from application import db

post = Blueprint('post', __name__)


def save_pic(form_pic):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_pic.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/images', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_pic)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


@post.route('/create', methods=['GET', 'POST'])
def create():
    form = PostForm()
    if form.validate_on_submit():
        if form.pic.data:
            picture_file = save_pic(form.pic.data)
        title = form.title.data
        subtitle = form.subtitle.data
        pic = picture_file
        body = form.body.data
        newpost = Post(title=title, subtitle=subtitle, pic=pic, body=body, author=current_user)
        db.session.add(newpost)
        db.session.commit()
        flash('New Post has been successfully created')
        return redirect(url_for('post.listposts'))
    return render_template('posts/create.html', form=form)


@post.route('/list')
def listposts():
    posts = Post.query.all()
    return render_template('posts/list.html', posts=posts)


@post.route('/viewpost/<int:post_id>')
def viewpost(post_id):
    singlepost = Post.query.filter_by(id=post_id).first()
    pic = url_for('static', filename='images/' + singlepost.pic)
    return render_template('posts/viewpost.html', post=singlepost, pic=pic)


@post.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form = PostForm()
    singlepost = Post.query.filter_by(id=id).first()
    if form.validate_on_submit():
        if form.pic.data:
            picture_file = save_pic(form.pic.data)
            singlepost.pic = picture_file
        singlepost.title = form.title.data
        singlepost.subtitle = form.subtitle.data

        singlepost.body = form.body.data
        db.session.commit()
        flash('Details successfully updated')
        return redirect(url_for('post.listposts'))
    form.title.data = singlepost.title
    form.subtitle.data = singlepost.subtitle
    form.pic.data = singlepost.pic
    form.body.data = singlepost.body
    pic = url_for('static', filename='images/' + singlepost.pic)
    return render_template('posts/update.html', form=form, pic=pic)


@post.route('/delete/<int:id>')
def delete(id):
    posttodelete = Post.query.filter_by(id=id).first()
    db.session.delete(posttodelete)
    db.session.commit()
    flash('Post has been removed')
    return redirect(url_for('post.listposts'))
