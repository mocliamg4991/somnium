# Generated by Django 3.2.9 on 2022-07-27 11:38

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subdivision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Наименование')),
                ('slug', models.SlugField()),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='organization.subdivision', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'Подразделение',
                'verbose_name_plural': 'Подразделении',
            },
        ),
        migrations.AddConstraint(
            model_name='subdivision',
            constraint=models.UniqueConstraint(fields=('parent', 'slug'), name='subdivision_unique'),
        ),
    ]
