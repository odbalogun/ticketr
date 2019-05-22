# Generated by Django 2.2.1 on 2019-05-14 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talents', '0002_bookings_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='budget_from',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='budget from'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='budget_to',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='budget to'),
        ),
    ]