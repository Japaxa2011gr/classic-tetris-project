# Generated by Django 3.1.3 on 2021-01-25 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classic_tetris_project', '0032_auto_20201226_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='qualifier',
            name='review_data',
            field=models.JSONField(default=dict),
        ),
    ]