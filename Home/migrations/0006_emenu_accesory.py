# Generated by Django 4.0.6 on 2022-08-27 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_shop_followers_alter_shop_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.shop')),
            ],
        ),
        migrations.CreateModel(
            name='Accesory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('price', models.IntegerField()),
                ('emenu', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.emenu')),
            ],
        ),
    ]
