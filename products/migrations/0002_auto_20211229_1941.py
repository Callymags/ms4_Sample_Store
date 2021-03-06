# Generated by Django 3.2 on 2021-12-29 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='image_back',
        ),
        migrations.AddField(
            model_name='product',
            name='image_front',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
