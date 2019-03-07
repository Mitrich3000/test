from django.db import models


class District(models.Model):
    name = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Retail(models.Model):
    name = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Сеть предприятий"
        verbose_name_plural = "Сети предприятий"

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=30)
    retail = models.ForeignKey(Retail, on_delete=models.CASCADE)
    description = models.TextField(blank=True, verbose_name="Описание")
    district = models.ManyToManyField(District)

    class Meta:
        verbose_name = "Предприятие"
        verbose_name_plural = "Предприятия"

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    organization = models.ManyToManyField(Organization)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class Price(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"

    def __str__(self):
        return f'Цена {self.product} на {self.organization}'
