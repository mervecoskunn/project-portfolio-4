import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50, verbose_name=_('First Name'),
                                  help_text=_('First Name'))
    last_name = models.CharField(max_length=50, verbose_name=_('Last Name'),
                                 help_text=_('Last Name'))
    email = models.EmailField(_("email address"), blank=True, unique=True)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.get_full_name() if self.get_full_name() != '' else self.get_username()

    def save(self, *args, **kwargs):
        self.first_name = str(self.first_name).strip().title()
        self.last_name = str(self.last_name).strip().upper()
        super(User, self).save(*args, **kwargs)
