from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("""
        <h1>Это страница DATA моего первого проекта на Django</h1>
        <p>Добро пожаловать на главную страницу моего Django-проекта.</p>
        <p>Вы можете посетить другие страницы:</p>
        <ul>
            <li><a href="/myapp/data/">Страница Data</a> - информация о проекте</li>
            <li><a href="/myapp/test/">Страница Test</a> - другая тестовая страница</li>
        </ul>
        <p>Для администрирования перейдите по адресу <a href="/admin/">админ-панели</a>.</p>
        <p>Удачи с изучением Django!</p>
    """)

def data(request):
    return HttpResponse("<h1>Это страница DATA моего первого проекта на Django</h1>")

def test(request):
    return HttpResponse("<h2>Это страница TEST моего первого проекта на Django</h2>")