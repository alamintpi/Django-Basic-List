# Generated by Django 3.0.7 on 2020-07-08 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QueryApp', '0009_auto_20200708_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
