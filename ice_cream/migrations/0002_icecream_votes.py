# Generated by Django 2.2.6 on 2019-10-09 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='icecream',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
