from django.urls import path
from posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.CategoryListView.as_view(), name='home'),

    path('create', views.PostCreateView.as_view(), name='post_create'),
    path('<uuid:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('posts', views.PostListView.as_view(), name='post_list'),
    path('<uuid:pk>/edit', views.PostEditView.as_view(), name='post_edit'),
    path('<uuid:pk>/delete', views.PostDeleteView.as_view(), name='post_delete'),

    path('categories', views.CategoryListView.as_view(), name='category_list'),
    path('categories/<uuid:pk>', views.CategoryDetailView.as_view(), name='category_detail'),

    path('<uuid:post_id>/comment', views.CommentCreateView.as_view(), name='comment_create'),
    path('manage/<uuid:pk>', views.ManagePostView.as_view(), name='manage_posts'),
    path('user/<uuid:pk>', views.UserPageView.as_view(), name='user_page'),
]
