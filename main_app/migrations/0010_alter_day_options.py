# Generated by Django 4.0.4 on 2022-04-27 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_day_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='day',
            options={'ordering': ['day']},
        ),
    ]