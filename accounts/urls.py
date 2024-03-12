from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="accounts/logout.html"), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
]
