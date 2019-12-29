from django.contrib import admin
from django.urls import path, include
import back_1.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('back_1.urls')),
]
