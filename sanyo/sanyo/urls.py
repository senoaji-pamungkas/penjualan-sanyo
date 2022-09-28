from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from konsumen.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index, name='Index'),
    path('order/', Order, name='Order'),
    path('order/create/', Create, name='create'),
    path('service/', Service, name='Service'),
    path('office/', Office, name='Office')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
