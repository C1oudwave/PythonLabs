
from django.contrib import admin
from django.urls import path
from AFR import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='first'),
]
