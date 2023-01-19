from flask import render_template, Blueprint
from flask import request

from dao.dao import PostsDAO


posts_path = './data/posts.json'
comments_path = './data/comments.json'
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='./templates')
posts = PostsDAO('./data/posts.json', './data/comments.json')

@main_blueprint.route('/')
def index_page():
    all_posts = posts.get_all_posts()
    return render_template('index.html', posts=all_posts)

@main_blueprint.route('/posts/<int:postid>')
def post_page(postid):
    found_post = posts.get_post_by_pk(postid)
    comments = posts.get_comments_by_post_id(postid)
    return render_template('post.html', post=found_post, comments=comments)

@main_blueprint.route('/search', methods=['GET'])
def search_page():
    query = request.args.get('s')
    found_posts = posts.search_posts(query)
    return render_template('search.html', posts=found_posts, substr=query)

@main_blueprint.route('/users/<username>', methods=['GET'])
def user_page():
    user_posts = posts.get_posts_by_username(username)
    return render_template('search.html', posts=user_posts, username=username)
