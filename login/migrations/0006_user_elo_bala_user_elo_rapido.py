# Generated by Django 4.1.1 on 2022-11-06 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_alter_user_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='elo_bala',
            field=models.IntegerField(blank=True, default=1500),
        ),
        migrations.AddField(
            model_name='user',
            name='elo_rapido',
            field=models.IntegerField(blank=True, default=1500),
        ),
    ]