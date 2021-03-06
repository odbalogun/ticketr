# Generated by Django 2.2.1 on 2019-06-09 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=100, null=True, verbose_name='first name')),
                ('last_name', models.CharField(max_length=100, null=True, verbose_name='last name')),
            ],
        ),
    ]
