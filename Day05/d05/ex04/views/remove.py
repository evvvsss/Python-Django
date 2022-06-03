from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from ..forms import RemoveForm
import psycopg2


class Remove(View):
    template = 'ex05/remove.html'
    connection = psycopg2.connect(
        dbname=settings.DATABASES['default']['NAME'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        host=settings.DATABASES['default']['HOST'],
        port=settings.DATABASES['default']['PORT'],
    )


    def get(self, request):
        try:
            self.connection.autocommit = True
            with self.connection.cursor() as cursor:
                cursor.execute("""
                            SELECT * FROM ex04_movies""")
                movies = cursor.fetchall()
            context = {'form': RemoveForm(choices=((movie[0], movie[0]) for movie in movies))}
            return render(request, self.template, context)
        except Exception as e:
            print(e)
            return HttpResponse("No data available")


    def post(self, request):
        try:
            self.connection.autocommit = True
            with self.connection.cursor() as cursor:
                cursor.execute("""
                            SELECT title FROM ex04_movies""")
                movies = cursor.fetchall()
            choices = ((movie[0], movie[0]) for movie in movies)
        except Exception as e:
            print(e)
        rem_form = RemoveForm(choices, request.POST)
        if rem_form.is_valid() == True:
            try:
                with self.connection.cursor() as cursor:
                    cursor.execute("""
                                      DELETE FROM ex04_movies WHERE title = %s""", [rem_form.cleaned_data['title']])
                    self.connection.commit()
            except Exception as e:
                print(e)
        return redirect(request.path)



