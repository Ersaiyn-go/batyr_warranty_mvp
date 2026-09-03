from django.contrib import admin
from django.urls import path

from warranty.views import check_warranty

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', check_warranty, name='home'),
    path('warranty/', check_warranty, name='check_warranty'),
]