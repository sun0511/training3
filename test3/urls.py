from django.contrib import admin
from django.urls import re_path, path
from test3.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
]