from django.shortcuts import render
from django.views.generic import CreateView, DetailView, TemplateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from blog.models import *
# Create your views here.



class Home2detail(DetailView):
    model = Market
    template_name = 'home2_detail.html'

def salafan(request):
    malumot = Market.objects.all()
    return render (request, 'home2.html', {'malumotes':malumot})

def seryo(request):
    malumot = Seryo.objects.all()
    return render (request, 'seryo_srm.html', {'malumotes':malumot})

def aborud(request):
    malumot = Aborud.objects.all()
    return render (request, 'aborud_srm.html', {'malumotes':malumot})

class Malumotqushish(CreateView):
    model = Market
    template_name = 'plus.html'
    fields = ('title', 'body', 'holati', 'country', 'photo', 'rangi')


class SeryoQushish(CreateView):
    model = Seryo
    template_name = 'SeryoPlus.html'
    fields = ('title', 'body', 'photo', 'markasi')

class AborudQushish(CreateView):
    model = Aborud
    template_name = 'aborudqushish.html'
    fields = ('title', 'body', 'holati', 'photo')

class SotilganMahsulotlar(TemplateView):
    template_name = 'sotilganmahsulotlar.html'


