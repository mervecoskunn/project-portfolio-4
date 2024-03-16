from django.db.models.signals import post_save
from django.dispatch import receiver

from posts import models


@receiver(post_save, sender=models.Post)
def post_created_notify(sender, instance, **kwargs):
    if kwargs.get('created') is True:
        models.Notification.objects.create(title='Published New Post',
                                           body=f'The post titled {instance.title} was published')
