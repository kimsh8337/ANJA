# Generated by Django 2.2.16 on 2020-11-17 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('station_cd', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('station_nm', models.CharField(max_length=20)),
                ('station_nm_eng', models.CharField(max_length=100)),
                ('station_nm_line', models.CharField(max_length=20)),
                ('station_cd_fr', models.CharField(max_length=20)),
            ],
        ),
    ]
