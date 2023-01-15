import pytest
from app import app
from dao.dao import PostsDAO

posts = PostsDAO('./data/posts.json', './data/comments.json')

keys_shold_be = {
    "poster_name",
    "poster_avatar",
    "pic",
    "content",
    "views_count",
    "likes_count",
    "pk",
}


def test_api_all_posts():
    response = app.test_client().get('/api/posts')
    assert response.status_code == 200
    api_response = response.json
    assert type(api_response) ==list
    assert set(api_response[0].keys()) == keys_shold_be

def test_api_post():
    response = app.test_client().get('/api/posts/1')
    assert response.status_code == 200
    api_response = response.json
    assert type(api_response) == dict
    assert set(api_response[0].keys()) == keys_shold_be
