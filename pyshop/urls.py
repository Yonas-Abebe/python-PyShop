from django.contrib import admin
from django.urls import path, include
from products import views   # import index & new views
from products.views import deploy   # import deploy view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('', views.index, name='home'),
    path('deploy/', deploy),
]
