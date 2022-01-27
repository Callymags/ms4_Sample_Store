# Generated by Django 3.2 on 2022-01-23 13:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('slug', models.SlugField(unique=True)),
                ('intro', models.TextField(max_length=254)),
                ('body', models.TextField(validators=[django.core.validators.MinLengthValidator(15)])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('author', models.CharField(blank=True, max_length=254, null=True)),
                ('tags', models.ManyToManyField(blank=True, to='blog.Tag')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
