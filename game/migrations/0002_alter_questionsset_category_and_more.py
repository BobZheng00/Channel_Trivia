# Generated by Django 4.0.6 on 2022-08-10 16:59

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionsset',
            name='category',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='questionsset',
            name='correct_answer',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='questionsset',
            name='incorrect_answer',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200, null=True), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='questionsset',
            name='type',
            field=models.CharField(max_length=200),
        ),
    ]
