# Generated by Django 3.0.7 on 2020-09-18 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ukumbi', '0004_auto_20200918_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
