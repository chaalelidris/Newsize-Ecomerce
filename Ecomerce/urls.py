from django.conf.urls.static import static
from Ecomerce.settings import MEDIA_URL
from django.conf import settings
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('',include('core.urls')),
    path('product/',include('products.urls')),
    path('order/',include('order.urls')),
    path('cart/',include('cart.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
