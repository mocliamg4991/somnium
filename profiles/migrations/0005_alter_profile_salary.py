# Generated by Django 3.2.9 on 2022-07-27 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20220727_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Ставка'),
        ),
    ]
