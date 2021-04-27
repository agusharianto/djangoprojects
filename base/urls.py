from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('film/', include('film.urls',namespace='film')),
    path('help/', views.help, name='help'),
    path('', views.index, name='index'),
]
