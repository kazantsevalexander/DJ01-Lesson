from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("""
        <h1>Это мой первый проект на Django</h1>
        <p>Вы можете посетить следующие страницы:</p>
        <ul>
            <li><a href="/myapp/">Страница проверки домашнего задания</a> - перейдите для проверки</li>
        </ul>
        <p>Для администрирования перейдите по адресу <a href="/admin/">админ-панели</a>.</p>
        <p>Удачи с изучением Django!</p>
    """)

def new(request):
    return HttpResponse("<h1>Это вторая страница моего проекта на Django</h1>")
