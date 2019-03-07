from rest_framework.serializers import ModelSerializer

from .models import District, Category, Retail, Organization, Products, Price


class DistrictSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = ('name')


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name')


class RetailSerializer(ModelSerializer):
    class Meta:
        model = Retail
        fields = ('name')


class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = ('name', 'description', 'retail', 'district')


class ProductsSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = ('name', 'category', 'organization')

class PriceSerializer(ModelSerializer):
    class Meta:
        model = Price
        fields = ('organization', 'product', 'price')