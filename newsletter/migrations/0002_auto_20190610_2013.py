# Generated by Django 2.2.1 on 2019-06-10 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscribers',
            options={'verbose_name': 'subscriber', 'verbose_name_plural': 'subscribers'},
        ),
        migrations.RemoveField(
            model_name='subscribers',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='subscribers',
            name='last_name',
        ),
    ]