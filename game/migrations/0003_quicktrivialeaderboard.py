# Generated by Django 4.0.6 on 2022-08-19 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0002_alter_questionsset_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuickTriviaLeaderboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('attempt', models.IntegerField(default=10)),
                ('category', models.CharField(max_length=100)),
                ('completed', models.DateTimeField(blank=True, null=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
