# Generated by Django 3.2.16 on 2023-01-15 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_showing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showing',
            name='duration',
            field=models.CharField(max_length=100),
        ),
    ]
