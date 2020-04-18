from __future__ import unicode_literals

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', admin.site.urls),
]
