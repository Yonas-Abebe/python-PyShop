from django.contrib import admin
from django.urls import path, include
from products import views   # <-- Add this import
from .deploy import deploy


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('', views.index, name='home'),
    path('deploy/', deploy),  # <-- add this
]
