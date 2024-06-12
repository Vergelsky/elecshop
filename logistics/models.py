from django.db import models


class SupplyChainParticipant(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=300, verbose_name='Улица')
    building = models.CharField(max_length=100, verbose_name='Дом')
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Поставщик')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Продукт')
    debt = models.DecimalField(max_digits=14, decimal_places=2, verbose_name='Задолженность')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_factory = models.BooleanField(default=False, verbose_name='Это завод')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.supplier:
            self.is_factory = True
        if self.is_factory:
            self.supplier = None
        super().save( *args, **kwargs)

    class Meta:
        verbose_name = 'Участник цепи поставок'
        verbose_name_plural = 'Участники цепи поставок'


class Product(models.Model):
    name = models.CharField(max_length=600, verbose_name='Название')
    model = models.CharField(max_length=600, verbose_name='Модель')
    date = models.DateField(verbose_name='Дата производства')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'
