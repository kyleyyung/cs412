# Generated by Django 4.2.16 on 2024-11-18 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0003_product_seller_delete_sell"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="seller",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="project.user"
            ),
        ),
    ]