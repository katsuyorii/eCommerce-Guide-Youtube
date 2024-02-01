from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Наименование:', max_length=150, unique=True)
    slug = models.SlugField(verbose_name='Слаг', unique=True, blank=True, null=True, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name