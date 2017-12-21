# Generated by Django 2.0 on 2017-12-21 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20171023_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='long_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='note_field',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
