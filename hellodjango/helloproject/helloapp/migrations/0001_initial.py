# Generated by Django 5.0.4 on 2024-04-04 10:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('decsription', models.TextField()),
                ('intake_date', models.DateTimeField(auto_now_add=True)),
                ('shelter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='helloapp.shelter')),
            ],
        ),
    ]
