# Generated by Django 3.0.7 on 2020-09-19 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ukumbi', '0006_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Image',
        ),
    ]
