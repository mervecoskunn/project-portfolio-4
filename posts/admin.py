from django.contrib import admin
from posts import models
from django.utils.translation import gettext_lazy as _


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    search_help_text = _('Search by name')


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'author', 'category', 'is_approved','created_on', 'last_modified')
    list_filter = ('is_approved', 'created_on', 'last_modified')
    search_fields = ('title', 'body')
    search_help_text = _('Search by title or body')


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('author', 'post')
    search_help_text = _('Search by author or post')


@admin.register(models.Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'body', 'created_on')
    list_filter = ('created_on',)
