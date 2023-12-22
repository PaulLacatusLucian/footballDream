from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.urls import include

from base.views import home, room

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls'))
]

