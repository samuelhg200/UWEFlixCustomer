# Generated by Django 3.2.16 on 2023-01-15 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Showing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('age_rating', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
    ]
