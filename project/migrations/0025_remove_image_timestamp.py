# Generated by Django 4.2.16 on 2024-12-04 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0024_alter_product_price"),
    ]

    operations = [
        migrations.RemoveField(model_name="image", name="timestamp",),
    ]
