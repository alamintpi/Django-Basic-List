# Generated by Django 3.0.7 on 2020-06-22 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QueryApp', '0010_auto_20200622_0557'),
    ]

    operations = [
        migrations.CreateModel(
            name='fileupload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filesize', models.FileField(upload_to='')),
            ],
        ),
    ]