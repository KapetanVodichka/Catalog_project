from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    # created_at = models.DateField(default=timezone.now, verbose_name='дата создания')

    def __str__(self):
        return f'{self.name}: {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    image = models.ImageField(upload_to='image/', verbose_name='Изображение (превью)', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за покупку')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    last_date_changing = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name}: {self.category}, {self.price}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('name',)


class Contacts(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя')
    phone = models.IntegerField(verbose_name='телефон')
    message = models.TextField(verbose_name='сообщение')

    def __str__(self):
        return f'{self.name} ({self.phone}): {self.message}'

    class Meta:
        verbose_name = 'контактное лицо'
        verbose_name_plural = 'контактные лица'


class ProductVersion(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_num = models.TextField(verbose_name='номер версии', unique=True, null=True, blank=True)
    version_name = models.CharField(max_length=150, verbose_name='название версии')
    active_version = models.BooleanField(verbose_name='активная версия', default=False)

    def __str__(self):
        return f'{self.version_name} ({self.version_num})'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
