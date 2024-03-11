from django.contrib.auth.forms import BaseUserCreationForm

from django.contrib.auth import get_user_model


class RegisterForm(BaseUserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'email',)
