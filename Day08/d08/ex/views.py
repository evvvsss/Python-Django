from django.shortcuts import render
from django.views.generic import FormView, ListView
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Image
from .forms import ImageForm

class Init(ListView, FormView):
    success_url = reverse_lazy('init')
    template_name = 'init.html'
    form_class = ImageForm
    model = Image
    queryset = model.objects.all().order_by('-id')

    def form_valid(self, form: ImageForm):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form: ImageForm):
        print(form.errors)
        return super().form_invalid(form)

