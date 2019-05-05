# Generated by Django 2.2.1 on 2019-05-04 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('deals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deals',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='deals',
            name='options',
            field=models.ManyToManyField(through='deals.DealCategories', to='deals.Categories'),
        ),
        migrations.AddField(
            model_name='dealcategories',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deals.Categories'),
        ),
        migrations.AddField(
            model_name='dealcategories',
            name='deal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deals.Deals'),
        ),
    ]
