# Generated by Django 5.0.4 on 2024-04-22 04:58

import users.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_staff_user_is_superuser_user_last_login'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.models.MyAccountManager()),
            ],
        ),
    ]