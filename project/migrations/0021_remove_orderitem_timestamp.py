# Generated by Django 4.2.16 on 2024-12-01 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0020_alter_orderitem_timestamp"),
    ]

    operations = [
        migrations.RemoveField(model_name="orderitem", name="timestamp",),
    ]