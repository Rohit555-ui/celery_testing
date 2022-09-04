from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('celerytask', views.CeleryTask.as_view()),
    path('redis', views.RedisConnect.as_view()),
]