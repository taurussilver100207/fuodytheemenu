# Generated by Django 4.0.6 on 2022-08-28 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0019_order_userconfirm_alter_order_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='order',
            name='num',
            field=models.IntegerField(default='96826'),
        ),
    ]