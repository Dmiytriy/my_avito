# Generated by Django 4.1.5 on 2023-01-24 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('lat', models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True)),
                ('lng', models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True)),
            ],
            options={
                'verbose_name': 'Местоположение',
                'verbose_name_plural': 'Местоположения',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('member', 'пользователь'), ('moderator', 'модератор'), ('admin', 'админ')], max_length=9)),
                ('age', models.PositiveSmallIntegerField()),
                ('location', models.ManyToManyField(to='users.location')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['username'],
            },
        ),
    ]
