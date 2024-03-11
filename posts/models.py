import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    """
    A category for classifying posts.
    """
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    name = models.CharField(
        max_length=50, verbose_name=_('Name'),
        help_text=_('Enter the name of the category.')
    )
    body = models.TextField(
        verbose_name=_('Body'),
        help_text=_('Enter the body of your category.'),
    )
    image = models.ImageField(upload_to='media/categories/%Y/%m/%d', verbose_name=_('Image'), help_text=_('Image'))

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    A blog post with a title, body, creation date, modification date, author, and associated categories.
    """
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    title = models.CharField(
        max_length=255,
        verbose_name=_('Title'),
        help_text=_('Enter the title of your post.'),
    )
    body = models.TextField(
        verbose_name=_('Body'),
        help_text=_('Enter the body of your post.'),
    )
    is_approved = models.BooleanField(
        default=False,
        verbose_name=_('Approved'),
        help_text=_('Whether the post is approved or not.'),
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created On'),
        help_text=_('The date and time the post was created.'),
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Last Modified'),
        help_text=_('The date and time the post was last modified.'),
    )
    author = models.ForeignKey(
        get_user_model(), verbose_name=_('Author'),
        help_text=_('Post creator'),
        on_delete=models.PROTECT,
        related_name='user_posts'
    )
    image = models.ImageField(upload_to='media/posts/%Y/%m/%d', verbose_name=_('Image'), help_text=_('Image'))
    category = models.ManyToManyField(
        Category,
        verbose_name=_('Categories'),
        help_text=_('Categories')
    )

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    A comment on a post, with an author, post, body, and creation date.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='user_comments',
        verbose_name=_('Comment Creator'),
        help_text=_('Comment creator')
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.PROTECT,
        related_name='post_comments', verbose_name=_('Post'),
        help_text=_('Select the post to which this comment will be associated.')
    )
    body = models.TextField()
    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created On'),
        help_text=_('The date and time the comment was created.'),
    )

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
        ordering = ('-created_on',)

    def __str__(self):
        return self.post.__str__()


class Like(models.Model):
    """
    A like on a post, with an author and post.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='user_likes')
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='post_likes')

    class Meta:
        unique_together = ('author', 'post')
        verbose_name = _('Like')
        verbose_name_plural = _('Likes')

    def __str__(self):
        return self.post.__str__()
