# Generated by Django 4.0.6 on 2022-08-28 03:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home', '0013_alter_order_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='num',
            field=models.IntegerField(default='89946'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderer', to=settings.AUTH_USER_MODEL),
        ),
    ]
