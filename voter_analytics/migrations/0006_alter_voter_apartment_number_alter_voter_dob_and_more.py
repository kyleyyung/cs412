# Generated by Django 4.2.16 on 2024-11-09 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("voter_analytics", "0005_remove_voter_voter_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="voter", name="apartment_number", field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="voter", name="dob", field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="voter", name="dor", field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="voter", name="zipcode", field=models.IntegerField(),
        ),
    ]
