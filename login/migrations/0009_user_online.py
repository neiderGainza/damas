# Generated by Django 4.1.1 on 2022-11-10 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_rename_elo_bala_user_elo_remove_user_elo_rapido'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='online',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
