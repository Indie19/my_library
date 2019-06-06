# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-12 04:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20190412_0309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('death_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.Author'),
        ),
    ]
