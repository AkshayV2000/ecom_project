# Generated by Django 4.1.3 on 2023-01-12 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=20)),
                ('customer_email', models.CharField(max_length=20)),
                ('customer_password', models.CharField(max_length=10)),
                ('customer_addres', models.CharField(default='', max_length=40)),
                ('customer_gender', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_name', models.CharField(max_length=20)),
                ('seller_address', models.CharField(max_length=100)),
                ('seller_phone', models.BigIntegerField()),
                ('seller_email', models.CharField(max_length=30)),
                ('seller_companyname', models.CharField(max_length=20)),
                ('seller_accholdername', models.CharField(max_length=20)),
                ('seller_ifsc', models.CharField(max_length=15)),
                ('seller_branch', models.CharField(max_length=20)),
                ('seller_accno', models.BigIntegerField()),
                ('seller_username', models.CharField(max_length=20)),
                ('seller_password', models.CharField(max_length=20)),
                ('seller_pic', models.ImageField(upload_to='seller/')),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
    ]
