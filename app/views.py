from django.http import HttpResponse
from django.utils import timezone
import os

def home_view(request):
    # Список доступных страниц
    pages = [
        '<a href="/current_time/">Текущее время</a>',
        '<a href="/workdir/">Рабочая директория</a>'
    ]
    response_html = "<h1>Главная страница</h1><p>Доступные страницы:</p>" + "<br>".join(pages)
    return HttpResponse(response_html)

def current_time_view(request):
    # Получение текущего времени
    now = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"<h1>Текущее время: {now}</h1>")

def workdir_view(request):
    # Получение содержимого рабочей директории
    workdir = os.getcwd()
    files = os.listdir(workdir)
    files_list = "<br>".join(files)
    return HttpResponse(f"<h1>Рабочая директория: {workdir}</h1><p>Содержимое:</p><pre>{files_list}</pre>")