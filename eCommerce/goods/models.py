from django.db import models
from pytils.translit import slugify


class Category(models.Model):
    name = models.CharField(verbose_name='Наименование:', max_length=150, unique=True)
    slug = models.SlugField(verbose_name='Слаг', unique=True, blank=True, null=True, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    '''
    Переопределение метода сохранения записи.
    С помощью библиотеки pytils мы переводим киррилицу в латиницу по полю name.
    Авто-слаг, при добавлении в конец слага добавляется id.
    '''
    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.name) + '-' + str(self.pk)
            super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(verbose_name='Наименование:', max_length=150, unique=True)
    slug = models.SlugField(verbose_name='Слаг', unique=True, blank=True, null=True, db_index=True)
    desc = models.TextField(verbose_name='Описание:')
    image = models.ImageField(verbose_name='Изображение:', upload_to='goods_images', null=True, blank=True)
    price = models.DecimalField(verbose_name='Цена:', default=0.00, decimal_places=2, max_digits=7)
    discount = models.DecimalField(verbose_name='Скидка:', default=0.00, decimal_places=2, max_digits=7, help_text='В процентах (%)')
    count = models.PositiveIntegerField(verbose_name='Количество на складе:', default=0)
    category = models.ForeignKey(verbose_name='Категория:', to=Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.name) + '-' + str(self.pk)
            super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name