# Generated by Django 4.0.6 on 2022-08-28 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0010_order_user_shop_is_real_time_alter_order_accesory'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='num',
            field=models.IntegerField(default='64884'),
        ),
    ]
