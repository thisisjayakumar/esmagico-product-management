from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product_management/', include('product_management.urls', namespace='product_management')),
]