from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('firstpage.urls')),
    path('admin/', admin.site.urls),
    path('hello', include('firstpage.urls')),
]
