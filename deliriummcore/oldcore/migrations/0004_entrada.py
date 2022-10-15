# Generated by Django 4.1.1 on 2022-10-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oldcore', '0003_alter_seller_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('created', models.DateTimeField(auto_now=True)),
                ('isCortesia', models.BooleanField(default=False)),
            ],
        ),
    ]
