from django.contrib import admin
from django.urls import path
from app.views import home_view, current_time_view, workdir_view

urlpatterns = [
    path('', home_view, name='home'),  # Главная страница
    path('current_time/', current_time_view, name='current_time'),  # Текущие время
    path('workdir/', workdir_view, name='workdir'),  # Рабочая директория
    path('admin/', admin.site.urls),
]