from django.contrib import admin
from django.urls import path, include
from backend.core.views import CategoryViewSet, SubcategoryViewSet, ProductViewSet, PurchaseViewSet, UserViewSet, FeedbackViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubcategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'purchases', PurchaseViewSet)
router.register(r'users', UserViewSet)
router.register(r'feedbacks', FeedbackViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
