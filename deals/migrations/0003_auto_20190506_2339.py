# Generated by Django 2.2.1 on 2019-05-06 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0002_auto_20190506_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealcategories',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price'),
        ),
    ]
