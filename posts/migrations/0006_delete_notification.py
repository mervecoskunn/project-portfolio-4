# Generated by Django 4.2.11 on 2024-03-18 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_notification_body_alter_notification_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
