# Generated by Django 2.1.4 on 2019-05-14 14:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190508_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_category', models.CharField(max_length=200)),
                ('category_summary', models.CharField(max_length=200)),
                ('category_slug', models.CharField(default=1, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='event_slug',
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_location',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_published',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.DateTimeField(verbose_name='event time'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.EventCategory', verbose_name='Category'),
        ),
    ]
