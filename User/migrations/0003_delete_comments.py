# Generated by Django 4.2.2 on 2023-06-09 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("User", "0002_comments"),
    ]

    operations = [
        migrations.DeleteModel(name="Comments",),
    ]