# Generated by Django 4.2.16 on 2024-10-19 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mini_fb", "0002_statusmessage"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(blank=True, upload_to="")),
                ("timestamp", models.DateTimeField(auto_now=True)),
                (
                    "message",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mini_fb.statusmessage",
                    ),
                ),
            ],
        ),
    ]