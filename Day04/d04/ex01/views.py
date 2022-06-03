from django.shortcuts import render
import requests


def index(request):
    r = requests.get("https://www.markdownguide.org/basic-syntax/")
    html = r.text
    with open("ex00/templates/ex00/index.html", "w") as f:
        f.write(html)
    return render(request, 'ex00/index.html')

def django(request):
    return render(request, 'ex01/django.html')

def display(request):
    return render(request, 'ex01/display.html')

def templates(request):
    r = requests.get("https://www.markdownguide.org/basic-syntax/")
    html = r.text
    with open("ex00/templates/ex00/index.html", "w") as f:
        f.write(html)
    return render(request, 'ex01/template.html')
