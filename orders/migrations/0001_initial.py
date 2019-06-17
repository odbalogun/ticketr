# Generated by Django 2.2.1 on 2019-06-17 00:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('code', models.CharField(max_length=50, verbose_name='order code')),
                ('status', models.CharField(default='open', max_length=50, verbose_name='status')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
                ('payment_status', models.CharField(default='pending', max_length=50, verbose_name='payment status')),
                ('payment_reference', models.CharField(blank=True, max_length=50, null=True, verbose_name='payment reference')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('object_id', models.PositiveIntegerField()),
                ('quantity', models.IntegerField(verbose_name='quantity')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='unit price')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.Order')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
