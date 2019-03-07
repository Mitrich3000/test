from django_filters import rest_framework as filters

from .models import Products, Price


class PriceFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Price
        fields = ['min_price', 'max_price']


class ProductFilter(filters.FilterSet):
    category = filters.NumberFilter(field_name="category__id", lookup_expr='iexact')

    class Meta:
        model = Products
        fields = ['category__id',]
