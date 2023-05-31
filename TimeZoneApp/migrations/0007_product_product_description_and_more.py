# Generated by Django 4.1.3 on 2023-01-31 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeZoneApp', '0006_product_product_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_description',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='product_thumbnail',
            field=models.ImageField(upload_to='media/TimeZoneApp/Thumbnails<function user_directory_path at 0x7fb828f24a60>'),
        ),
    ]