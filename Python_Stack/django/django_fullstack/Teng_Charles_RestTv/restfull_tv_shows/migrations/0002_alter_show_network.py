# Generated by Django 3.2 on 2021-04-18 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restfull_tv_shows', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='network',
            field=models.CharField(max_length=50),
        ),
    ]