# Generated by Django 2.0.2 on 2018-05-19 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_auto_20180519_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practice',
            name='name',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
