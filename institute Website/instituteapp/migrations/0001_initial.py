# Generated by Django 4.1.4 on 2023-04-05 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='coursedata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_no', models.IntegerField()),
                ('course_name', models.CharField(max_length=40)),
                ('timing', models.TimeField()),
                ('starting_date', models.DateField()),
                ('duration', models.CharField(max_length=40)),
                ('fees', models.IntegerField()),
                ('trainer_name', models.CharField(max_length=40)),
            ],
        ),
    ]
