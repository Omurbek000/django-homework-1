# Generated by Django 5.1.4 on 2024-12-04 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название события')),
                ('description', models.TextField(verbose_name='Описание события')),
                ('event_date', models.DateTimeField(verbose_name='Дата проведения события.')),
                ('location', models.CharField(max_length=300, verbose_name='Местоположение события')),
            ],
        ),
    ]
