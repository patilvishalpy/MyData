# Generated by Django 4.1.4 on 2023-04-06 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instituteapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedbackdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mail', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=100)),
                ('messange', models.CharField(max_length=200)),
            ],
        ),
    ]
