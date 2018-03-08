from flask import render_template, redirect, url_for, request
from . import main
from ..models import Post
from .forms import PostForm
from .. import db


@main.route('/')
def markdown_tutorial():
    return redirect(url_for('.index', req_url='home'))


@main.route('/<path:req_url>', methods=['GET', 'POST'])
def index(req_url):
    print(req_url)
    if request.method == 'POST':
        form = PostForm()
        if form.validate_on_submit():
            post = Post.query.filter_by(url=req_url).first()
            if not post:
                post = Post()
            post.title = form.title.data
            post.body = form.text.data
            post.url = req_url
            db.session.add(post)
            db.session.commit()
            # 第一次输入内容时
            return redirect(url_for('main.index', req_url=req_url))
        else:
            post = Post.query.filter_by(url=req_url).first_or_404()
            form.title.data = post.title
            form.text.data = post.body
            # 对于内容点击编辑
            return render_template('edit.html', post=post, form=form)
    else:
        post = Post.query.filter_by(url=req_url).first()
        if not post:
            post = Post()
            post.url = req_url
            form = PostForm()
            # 第一次输入 url 时
            return render_template('edit.html', post=post, form=form)
        else:
            post = Post.query.filter_by(url=req_url).first_or_404()
            # 显示内容
            return render_template('index.html', post=post)
