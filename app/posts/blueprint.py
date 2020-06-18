from flask import Blueprint, render_template, request, redirect, url_for

from models import Post, Tag
from app import db
from .forms import PostForm

posts = Blueprint('blog', __name__, template_folder='templates')


# http://127.0.0.1:5000/blog/create
@posts.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        try:
            post = Post(title=title, body=body)
            db.session.add(post)
            db.session.commit()
        except:
            print('Something goes wrong')

        return redirect(url_for('blog.index'))

    else:
        form = PostForm()
        return render_template('posts/create_post.html', form=form)


@posts.route('/<slug>/edit', methods=['GET', 'POST'])
def edit_post(slug):
    post = Post.query.filter(Post.slug == slug).first()

    if request.method == 'POST':
        form = PostForm(formdata=request.form, obj=post)
        form.populate_obj(post)
        db.session.commit()

        return redirect(url_for('blog.post_detail', slug=post.slug))

    else:
        form = PostForm(obj=post)
        return render_template('posts/edit_post.html', post=post, form=form)


@posts.route('/')
def index():
    q = request.args.get('q')
    page = request.args.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    posts_query = Post.query
    if q:
        posts_query = posts_query.filter(Post.title.contains(q) | Post.body.contains(q))

    posts = posts_query.order_by(Post.created_date.desc())
    paginated_posts = posts.paginate(page=page, per_page=7)

    return render_template('posts/index.html', paginated_posts=paginated_posts, q=q)


@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first()
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags)


@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug == slug).first()
    posts = tag.posts.all()
    return render_template('posts/tag_detail.html', tag=tag, posts=posts)
