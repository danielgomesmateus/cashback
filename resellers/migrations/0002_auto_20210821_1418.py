# Generated by Django 3.2.6 on 2021-08-21 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resellers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='reseller',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='reseller',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='reseller',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
    ]