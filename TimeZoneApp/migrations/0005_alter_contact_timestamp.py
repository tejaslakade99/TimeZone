# Generated by Django 4.1.3 on 2023-01-30 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeZoneApp', '0004_product_alter_contact_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='timeStamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
