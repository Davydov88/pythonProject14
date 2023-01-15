import json

from dao.post import Post

class PostsDAO:
    def __int__(self, posts_path, comments_path):
        self.posts_path = posts_path
        self.comments_path = comments_path

    def load_posts(self):
        """Создаем метод, который открывает json файл"""
        with open(self.posts_path, 'r', encoding='utf-8') as file:
            new_posts = []
            posts_data = json.load(file)

            for post in posts_data:
                new_posts.append(Post(
                    post['poster_name'],
                    post['poster_avatar'],
                    post['pic'],
                    post['content'],
                    post['views_count'],
                    post['likes_count'],
                    post['pk']))
            return new_posts

    def get_all_posts(self):
        """создаем метод, который возвращает все посты"""
        return self.load_posts

    def get_post_by_pk(self, pk):
        """создаем метод, который возвращает посты определенного пользователя"""
        posts = self.load_posts()
        for post in posts:
            if post.pk == pk:
                return post
        return

    def load_posts(self):
        """Создаем метод, который открывает json файл"""
        with open(self.comments_path, 'r', encoding='utf-8') as file:
            comments = json.load(file)
        return comments

    def get_comments_by_post_id(self,post_id):
        """создаем метод, который возвращает комментарии определенного пользователя"""
        comments = self.load_comments()
        post_comments = []

        for comment in comments:
            if comment['post_id'] == post_id:
                post_comments.append(comment)
        return post_comments

    def search_posts(self, substr):
        """создаем метод, который возвращает посты по ключевому слову(подстроке)"""
        posts = self.load_posts()
        new_posts = []

        for post in posts:
            if substr.lower() in post.content.lower():
                new_posts.append(post)
        return new_posts

    def get_posts_by_username(self, username):
        """создаем метод, который возвращает посты по имени пользователя"""
        posts = self.load_posts()
        user_posts = []

        for post in posts:
            if post.poster_name.lower() == username.lower():
                user_posts.append(post)
        return user_posts

    def load_posts_json(self):
        """Создаем метод, который открывает json файл"""
        with open(self.posts_path, 'r', encoding='utf-8') as file:
            posts_data = json.load(file)
        return posts_data

    def get_post_by_pk_json(self,pk):
        posts = self.load_posts_json()
        for post in posts:
            if post['pk'] == pk:
                return post
        return