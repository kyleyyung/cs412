# Generated by Django 4.2.16 on 2024-11-29 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0011_alter_profile_user"),
    ]

    operations = [
        migrations.RemoveField(model_name="profile", name="user",),
    ]
