# Generated by Django 4.2 on 2023-05-26 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_alter_user_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=15)),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
