from django.shortcuts import render
from django.views import View
from .models import Supermercado, Produto

class InicialView(View):
    dados = {}
    template = 'principal/base.html'

    def get(self, request, **kwargs):
        return render(request, self.template, self.dados)
