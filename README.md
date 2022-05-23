# Python-Django

# bash commands:  
## Виртуальное окружение (в корневой папке):  
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

## Создание проекта и приложения:   
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
 
 ## Установка PostgreSQL  
 Сначала установим Brew:  
 curl -fsSL https://rawgit.com/kube/42homebrew/master/install.sh | zsh  
 
 Потом установим PostgreSQL:  
 brew install postgres  
 pg_ctl -D /usr/local/var/postgres start #запуск вручную  
 brew services restart postgresql #перезагрузка  
 
 Подключение к Postreesql:  
 psql -l  
 sudo psql -U Dream -d postgres  
 createdb dbname #создать ДБ  
 dropdb dbname #удалить ДБ  
 CREATE DATABASE dbname   
 dbname='stocks'  
 Сайт где все описано как работать с PostgreSQL: https://ploshadka.net/postgresql/
## SQL
Устанавливаем pgAdmin 4 - для создания БД. 
brew services restart postgresql 
## Миграции
 python manage.py makemigrations #берет текущие модели и по ним строит файл миграции
 python manage.py sqlmigrate model_name number_of_migration #
 python manage.py migrate  #берет этот файл и применяет ее к БД
