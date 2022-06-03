from django.conf import settings
from django.http import HttpRequest, HttpResponse
import psycopg2

#
# def index(request):
#     return render(request, 'ex00/index.html')


def init(request: HttpRequest):
    connection = None
    try:
        connection = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
        )                                                 # передаем параметры для подкл к БД
        connection.autocommit = True                    #для того чтобы запрос сработал и записался в БД
        # with connection.cursor() as cursor:             #объект который содержит методы для выполнения команд
        #     cursor.execute("SELECT version();")         #выполнение запроса (имя запроса)
        #     print(f'server version:{cursor.fetchone()}')#кортеж (tuple) запроса или None
        with connection.cursor() as cursor:
            # cursor.execute("""DROP TABLE IF EXISTS ex00_movies""")
            cursor.execute("""
                            CREATE TABLE IF NOT EXISTS ex00_movies(
                            title VARCHAR(64) UNIQUE NOT NULL,
                            episode_nb INT PRIMARY KEY,
                            opening_crawl TEXT,
                            director VARCHAR(32) NOT NULL,
                            producer VARCHAR(128) NOT NULL,
                            release_date DATE NOT NULL
                            );
                        """)
            print("Table created successfully")
            # connection.commit() #для того чтобы запрос сработал и записался в БД
    except Exception as ex:
        print("Error", ex)
    try:
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)
