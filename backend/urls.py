from django.contrib import admin
from django.urls import path, include

from backend.core.views import CategoryViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
