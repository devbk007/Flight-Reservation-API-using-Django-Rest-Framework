# Generated by Django 3.2.16 on 2022-12-17 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightApp', '0003_alter_passenger_middlename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='flightNumber',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='email',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
