# Generated by Django 4.2.16 on 2024-12-04 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0025_remove_image_timestamp"),
    ]

    operations = [
        migrations.AddField(
            model_name="image",
            name="timestamp",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
