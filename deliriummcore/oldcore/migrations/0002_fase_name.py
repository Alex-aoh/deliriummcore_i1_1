# Generated by Django 4.1.1 on 2022-10-11 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oldcore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fase',
            name='name',
            field=models.CharField(default='fase', max_length=20, verbose_name='Nombre de Fase'),
            preserve_default=False,
        ),
    ]
