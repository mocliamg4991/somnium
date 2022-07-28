from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Position(MPTTModel):
    name = models.CharField(max_length=100, unique=True, verbose_name='Наименование ')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительская категория')
    slug = models.SlugField()

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["parent", "slug"], name='position_unique'),
        ]
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name

class Subdivision(MPTTModel):
    name = models.CharField(max_length=100, unique=True, verbose_name='Наименование')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительская категория')
    slug = models.SlugField()

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["parent", "slug"], name='subdivision_unique'),
        ]
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

    def __str__(self):
        return self.name