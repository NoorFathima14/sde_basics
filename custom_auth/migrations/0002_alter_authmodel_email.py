# Generated by Django 5.1.7 on 2025-03-11 16:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("custom_auth", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="authmodel",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
