# Generated by Django 3.0.7 on 2020-06-27 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QueryApp', '0022_auto_20200627_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='birth_date',
        ),
    ]
