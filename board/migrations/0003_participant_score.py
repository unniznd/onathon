# Generated by Django 4.1.1 on 2022-09-06 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_participant'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
