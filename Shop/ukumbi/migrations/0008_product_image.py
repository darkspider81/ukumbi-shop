# Generated by Django 3.0.7 on 2020-09-19 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ukumbi', '0007_remove_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
