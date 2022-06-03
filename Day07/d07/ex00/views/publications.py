from typing import Any, Dict
from ..models import Article
from django.views.generic import ListView


class Publications(ListView):
    template_name = "ex00/publications.html"
    model = Article

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)