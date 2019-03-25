from django.http import Http404
from django_filters import rest_framework as filters
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from testdjangorest.filters import ProductFilter, PriceFilter
from .models import Organization, Products, Price
from .serializers import OrganizationSerializer, ProductsSerializer, PriceSerializer


class OrganizationDetail(APIView):
    def get_object(self, pk):
        try:
            return Organization.objects.get(pk=pk)
        except Organization.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        organization = self.get_object(pk)
        serializer = OrganizationSerializer(organization)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductsSerializer(product)
        return Response(serializer.data)


class OrganizationList(APIView):
    def get(self, request, format=None, district_id=1):
        organization = Organization.objects.filter(district=district_id)
        serializer = OrganizationSerializer(organization, many=True)
        return Response(serializer.data)


# filter by products
class ProductList(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter


# filter by price
class PriceList(ListAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PriceFilter
