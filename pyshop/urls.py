from django.contrib import admin
from django.urls import path, include
from products import views   # <-- Add this import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),

    # ★ Add homepage route to your products index ★
    path('', views.index),
]
