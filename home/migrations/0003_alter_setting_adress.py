# Generated by Django 4.1.4 on 2022-12-22 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_userprofile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="setting", name="adress", field=models.CharField(max_length=500),
        ),
    ]