from django.contrib import admin
from posts import models
from django.utils.translation import gettext_lazy as _


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    search_help_text = _('Search by name')


@admin.action(description=_('Disapprove selected posts'))
def not_approve_posts(modeladmin, request, queryset):
    queryset.update(is_approved=False)


@admin.action(description=_('Approve selected posts'))
def approve_posts(modeladmin, request, queryset):
    queryset.update(is_approved=True)


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'summary_body', 'author',
        'category', 'is_approved', 'created_on', 'last_modified'
    )
    list_filter = ('is_approved', 'created_on', 'last_modified')
    search_fields = ('title', 'body')
    search_help_text = _('Search by title or body')
    actions = (not_approve_posts, approve_posts)


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('author', 'post')
    search_help_text = _('Search by author or post')
