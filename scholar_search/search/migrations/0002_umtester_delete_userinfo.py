# Generated by Django 5.1.3 on 2024-11-25 03:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("search", "0001_initial"),
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
        migrations.DeleteModel(
            name="UserInfo",
        ),
    ]