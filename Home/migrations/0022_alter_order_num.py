# Generated by Django 4.0.6 on 2022-08-28 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0021_alter_order_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='num',
            field=models.IntegerField(default='96118'),
        ),
    ]
