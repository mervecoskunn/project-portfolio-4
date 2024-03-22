from django import forms
from posts import models


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control"}
    ))
    body = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control"}
    ))
    category = forms.ModelChoiceField(
        queryset=models.Category.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"})
    )
    image = forms.ImageField(widget=forms.FileInput(
        attrs={"class": "form-control"}
    ),
    )

    class Meta:
        model = models.Post
        fields = ('title', 'body', 'category', 'image')


class PostEditForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control"}
    ))
    body = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control"}
    ))
    category = forms.ModelChoiceField(
        queryset=models.Category.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        blank=True
    )
    image = forms.ImageField(widget=forms.FileInput(
        attrs={"class": "form-control"}),
    )

    class Meta:
        model = models.Post
        fields = ('title', 'body', 'category', 'image')


class CommentCreateForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control"}
    ))

    class Meta:
        model = models.Comment
        fields = ('body',)


class CommentEditForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control"}
    ))

    class Meta:
        model = models.Comment
        fields = ('body',)
