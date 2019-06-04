# Generated by Django 2.2.1 on 2019-06-04 12:23

from django.db import migrations, models
import movies.models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_cinema_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='image.jpg', upload_to=movies.models.movies_image_path, verbose_name='image'),
            preserve_default=False,
        ),
    ]
