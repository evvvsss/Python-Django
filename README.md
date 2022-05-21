# Python-Django

# bash commands:  
Виртуальное окружение (в корневой папке):  
/usr/local/bin/python3 -m venv local_lib  
source local_lib/bin/activate  
python3 -m pip install --upgrade pip  
pip3 install -r requirements.txt  #устанавливаем необходимые пакеты  

Чтобы выйти из  venv:  
deactivate  
   
 Посмотреть все установленные пакеты в окружении:  
 pip list. 
 
Все команды которые можно использовать:  
django-admin

 Создание проекта и приложения:   
django-admin startproject ptoject_name  
python manage.py startapp app_name  
python manage.py runserver #по умолч порт 8000, можно указать цифру после run-server для другого порта  
(ctrl+C  for exit)  


Потом переходим в папку приложения в apps.py,  копируем там класс.Для добавления приложения идем в папку проекта в settings.py и дописываем название приложения в список INSTALLED_APPS = [] пишем 'app_name.apps.App_NameConfig'

Все представления прописываем views.py:
from django.http import HttpResponse

def index(request):
 return HttpResponse("Добро пожаловать на страницу")

Для связывания этой функции с соответствующим URL адресом: идем в urls.py и там добавляем маршрут в urlpatterns:
path('app_name/', index)    #где index - ссылка на функцию представления( from app_name.views import index
 
  

