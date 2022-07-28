# Generated by Django 3.2.9 on 2022-07-26 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20220726_0757'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_images', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='code',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='patronymic',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Ставка'),
        ),
    ]