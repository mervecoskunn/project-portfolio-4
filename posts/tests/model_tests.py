from django.contrib.auth import get_user_model
from django.test import TestCase
from posts.models import Category, Post, Comment


class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Create a test category"""
        Category.objects.create(name="Test Category", body="This is a test category.")

    def test_category_name(self):
        """Test that the category name is correctly set"""
        category = Category.objects.get(name="Test Category")
        self.assertEqual(category.name, "Test Category")

    def test_category_body(self):
        """Test that the category body is correctly set"""
        category = Category.objects.get(name="Test Category")
        self.assertEqual(category.body, "This is a test category.")


class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Create a test user and post"""
        user = get_user_model()
        user = user.objects.create_user(username="testuser", password="secret")
        Post.objects.create(
            title="Test Post",
            body="This is a test post.",
            author=user,
        )

    def test_post_title(self):
        """Test that the post title is correctly set"""
        post = Post.objects.get(title="Test Post")
        self.assertEqual(post.title, "Test Post")

    def test_post_author(self):
        """Test that the post author is correctly set"""
        post = Post.objects.get(title="Test Post")
        self.assertEqual(post.author.username, "testuser")


class CommentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Create a test user, post and comment"""
        user = get_user_model()
        user = user.objects.create_user(username="testuser", password="secret")
        post = Post.objects.create(
            title="Test Post",
            body="This is a test post.",
            author=user,
        )
        Comment.objects.create(author=user, post=post, body="This is a test comment.")

    def test_comment_body(self):
        """Test that the comment body is correctly set"""
        comment = Comment.objects.get(body="This is a test comment.")
        self.assertEqual(comment.body, "This is a test comment.")

    def test_comment_post(self):
        """Test that the comment is associated with the correct post"""
        comment = Comment.objects.get(body="This is a test comment.")
        self.assertEqual(comment.post.title, "Test Post")
