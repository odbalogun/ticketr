# Generated by Django 2.2.1 on 2019-06-04 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('talents', '0006_auto_20190515_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=100, verbose_name='industry')),
            ],
            options={
                'verbose_name': 'industry',
                'verbose_name_plural': 'industries',
            },
        ),
        migrations.AlterField(
            model_name='bookingtalents',
            name='industry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='talents.Industry'),
        ),
    ]