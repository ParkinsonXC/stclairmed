# Generated by Django 2.0.2 on 2018-05-23 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20180523_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.CharField(default='0', max_length=2),
        ),
    ]
