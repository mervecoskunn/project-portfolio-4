from django import forms
from posts import models


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ('image', 'title', 'body', 'category')


class PostEditForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ('image', 'title', 'body', 'category')


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('body',)
