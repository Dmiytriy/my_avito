# Generated by Django 4.1.5 on 2023-01-29 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('member', 'пользователь'), ('moderator', 'модератор'), ('admin', 'админ')], default='member', max_length=9),
        ),
    ]