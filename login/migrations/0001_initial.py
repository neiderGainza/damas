# Generated by Django 4.1.1 on 2022-11-05 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.CharField(blank=True, default='Me gusta jugar damas!!!', max_length=1000)),
            ],
        ),
    ]
