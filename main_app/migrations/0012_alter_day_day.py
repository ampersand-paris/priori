# Generated by Django 4.0.4 on 2022-04-27 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_alter_task_description_alter_day_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='day',
            field=models.DateField(blank=True),
        ),
    ]