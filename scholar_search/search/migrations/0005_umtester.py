# Generated by Django 5.1.3 on 2024-11-27 05:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("search", "0004_delete_umtester"),
    ]

    operations = [
        migrations.CreateModel(
            name="umTester",
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
                ("username", models.CharField(max_length=32)),
                ("password", models.CharField(max_length=64)),
                ("major", models.CharField(max_length=64)),
            ],
        ),
    ]
