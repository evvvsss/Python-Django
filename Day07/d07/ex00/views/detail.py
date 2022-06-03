from typing import Any
from django import http
from django.http.response import HttpResponseBase
from ..forms import FavouriteForm
from ..models import Article
from django.views.generic import DetailView


class Detail(DetailView):
    template_name = "ex00/detail.html"
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = context['object']
        context["favouriteForm"] = FavouriteForm(article.id)
        return context