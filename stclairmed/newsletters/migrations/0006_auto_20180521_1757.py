# Generated by Django 2.0.5 on 2018-05-21 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0005_auto_20180521_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='pdf_img',
            field=models.ImageField(blank=True, height_field=620, upload_to='media', width_field=480),
        ),
    ]
