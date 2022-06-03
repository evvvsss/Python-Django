from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
import psycopg2

class Display(View):
    template = 'ex05/display.html'
    connection = psycopg2.connect(
        dbname=settings.DATABASES['default']['NAME'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        host=settings.DATABASES['default']['HOST'],
        port=settings.DATABASES['default']['PORT'],
    )

    def get(self, request):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM ex04_movies""")
                movies = cursor.fetchall()
            return render(request, self.template, {"movies": movies})
        except Exception as e:
            return HttpResponse("No data available")
