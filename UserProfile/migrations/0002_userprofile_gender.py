# Generated by Django 4.0.6 on 2022-08-03 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Not to mention', 'Not to mention')], default='Male', max_length=20),
        ),
    ]
