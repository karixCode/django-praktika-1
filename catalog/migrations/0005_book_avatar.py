# Generated by Django 3.2.25 on 2024-11-06 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_genre_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='avatar',
            field=models.ImageField(default=2, upload_to='catalog/books', verbose_name='Preview'),
            preserve_default=False,
        ),
    ]
