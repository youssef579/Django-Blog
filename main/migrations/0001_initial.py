# Generated by Django 4.1 on 2022-09-20 14:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('datetime', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ('-datetime',),
            },
        ),
    ]
