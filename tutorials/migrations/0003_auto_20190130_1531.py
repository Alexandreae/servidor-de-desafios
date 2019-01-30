# Generated by Django 2.1.4 on 2019-01-30 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0002_tutorialaccess_tutorial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorialaccess',
            name='last_access',
            field=models.DateTimeField(auto_now=True, verbose_name='first accessed'),
        ),
        migrations.AlterField(
            model_name='tutorialaccess',
            name='first_access',
            field=models.DateTimeField(auto_now_add=True, verbose_name='first accessed'),
        ),
    ]
