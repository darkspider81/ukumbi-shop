# Generated by Django 3.0.7 on 2020-09-18 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ukumbi', '0005_remove_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
