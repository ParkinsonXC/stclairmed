# Generated by Django 2.0 on 2018-05-20 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_rsvp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='num_guests',
            field=models.IntegerField(),
        ),
    ]