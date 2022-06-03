from django.shortcuts import render
from django.conf import settings
from django.http import HttpRequest, HttpResponse
import psycopg2

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
            cursor.execute("""
                            CREATE TABLE IF NOT EXISTS ex02_movies(
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


def populate(request: HttpRequest):
    try:
        connection = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
        )
        connection.autocommit = True
        movies = [
            {
                "episode_nb": 1,
                "title": "The Phantom Menace",
                "director": "George Lucas",
                "producer": "Rick McCallum",
                "release_date": "1999-05-19"
            },
            {
                "episode_nb": 2,
                "title": "Attack of the Clones",
                "director": "George Lucas",
                "producer": "Rick McCallum",
                "release_date": "2002-05-16"
            },
            {
                "episode_nb": 3,
                "title": "Revenge of the Sith",
                "director": "George Lucas",
                "producer": "Rick McCallum",
                "release_date": "2005-05-19"
            },
            {
                "episode_nb": 4,
                "title": "A New Hope",
                "director": "George Lucas",
                "producer": "Gary Kurtz, Rick McCallum",
                "release_date": "1977-05-25"
            },
            {
                "episode_nb": 5,
                "title": "The Empire Strikes Back",
                "director": "Irvin Kershner",
                "producer": "Gary Kurtz, Rick McCallum",
                "release_date": "1980-05-17"
            },
            {
                "episode_nb": 6,
                "title": "Return of the Jedi",
                "director": "Richard Marquand",
                "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum",
                "release_date": "1983-05-25"
            },
            {
                "episode_nb": 7,
                "title": "The Force Awakens",
                "director": "J. J. Abrams",
                "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
                "release_date": "2015-12-11"
            }
        ]
        INSERT_DATA = """
                INSERT INTO ex02_movies
                (
                    episode_nb,
                    title,
                    director,
                    producer,
                    release_date
                )
                VALUES
                (
                    %s, %s, %s, %s, %s
                )
                """
        result = []
        with connection.cursor() as cursor:
            for movie in movies:
                try:
                    cursor.execute(INSERT_DATA,
                        [
                            movie['episode_nb'],
                            movie['title'],
                            movie['director'],
                            movie['producer'],
                            movie['release_date'],
                        ]
                        )
                    result.append("OK")
                except psycopg2.DatabaseError as e:
                    connection.rollback()
                    result.append(e)
        return HttpResponse("<br/>".join(str(i) for i in result))
    except Exception as e:
        return HttpResponse(e)



def display(request: HttpRequest):
    try:
        connection = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT * FROM ex02_movies""")
            movies = cursor.fetchall()
        return render(request, 'ex03/display.html', {"movies": movies})
    except Exception as e:
        return HttpResponse("No data available")