# Generated by Django 4.0.4 on 2022-05-18 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsystem', '0019_delete_item'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Type',
            new_name='RoomType',
        ),
    ]