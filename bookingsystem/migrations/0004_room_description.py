# Generated by Django 4.0.4 on 2022-05-14 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsystem', '0003_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]