from django.conf import settings
from django.http import HttpRequest, HttpResponse
import psycopg2

def init(request: HttpRequest):
    try:
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)
