# Generated by Django 2.0.2 on 2018-05-30 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20180523_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='event',
            field=models.ForeignKey(on_delete='CASCADE', related_name='RSVPs', to='events.Event'),
        ),
    ]
