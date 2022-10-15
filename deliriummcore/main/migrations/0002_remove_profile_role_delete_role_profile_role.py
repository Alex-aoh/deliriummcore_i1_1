# Generated by Django 4.1.1 on 2022-10-07 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='role',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Usuario'), (2, 'RP'), (3, 'Staff'), (4, 'Organizador'), (5, 'Moderador'), (6, 'Administrador')], default=1, null=True),
        ),
    ]