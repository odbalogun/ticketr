# Generated by Django 2.2.1 on 2019-05-22 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0004_auto_20190515_1907'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dealcategories',
            options={'verbose_name': 'deal category', 'verbose_name_plural': 'deal categories'},
        ),
    ]