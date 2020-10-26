# Generated by Django 2.2.3 on 2019-09-17 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='bathrooms',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='bedrooms',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='city',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='garage',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='lot_size',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='sqft',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='state',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='zipcode',
        ),
        migrations.AlterField(
            model_name='listing',
            name='address',
            field=models.TextField(blank=True),
        ),
    ]