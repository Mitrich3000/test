from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/product/<int:pk>/', views.ProductDetail.as_view()),
    path('api/organization/<int:pk>/', views.OrganizationDetail.as_view()),
    path('api/organizations/<int:district_id>/', views.OrganizationList.as_view()),
    path('api/price/', views.PriceList.as_view()),
    path('api/products/', views.ProductList.as_view()),
]
