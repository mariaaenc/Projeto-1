from django.contrib import admin
from backend.core.models import User, Category, Purchase, Product, Address, Feedback, SubCategory
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(Address)
admin.site.register(Feedback)
admin.site.register(SubCategory)

