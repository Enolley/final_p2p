# Generated by Django 3.2.23 on 2023-11-27 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logreg', '0002_auto_20231127_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='course',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
