# Generated by Django 4.1.1 on 2022-11-10 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_user_partidas_jugadas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='elo_bala',
            new_name='elo',
        ),
        migrations.RemoveField(
            model_name='user',
            name='elo_rapido',
        ),
    ]