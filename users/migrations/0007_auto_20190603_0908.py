# Generated by Django 2.2.1 on 2019-06-03 09:08

from django.db import migrations, models
import users.managers


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190527_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
            managers=[
                ('objects', users.managers.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True, verbose_name='is staff'),
        ),
    ]
