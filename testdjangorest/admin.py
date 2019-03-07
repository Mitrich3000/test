from django.contrib import admin

from .models import District, Category, Retail, Organization, Products, Price

admin.site.register(District)
admin.site.register(Category)
admin.site.register(Retail)
admin.site.register(Organization)
admin.site.register(Products)
admin.site.register(Price)
