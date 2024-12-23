from django.shortcuts import render,redirect
from django.views.generic import CreateView, TemplateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import FoydalanuvchilarCreationForm
from .models import *
from django.db.models import Q

# Create your views here.
class SignUp(CreateView):
    form_class = FoydalanuvchilarCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# class Home(TemplateView):
#     template_name = 'home.html'
    


def search(request):
    query = request.GET.get('search')
    search_obj = Market.objects.filter(Q(title__icontains=query))
    return render(request, 'search.html', {'search_obj':search_obj, 'query':query})


def saved(request):
    # saqlash = Market.objects.all()
    saved = Market.objects.filter(saved=True)
    return render(request, 'saved.html', {'saved':saved})


def sklad(request):
    sklad = Market.objects.filter(sklad=True)
    return render(request, 'sklad.html', {'sklad':sklad})



def home(request):
    markets = Market.objects.order_by('-title')
    return render (request, 'home.html', {'markets':markets})

def category(request, id):  
    rangi = Category.objects.get(id=id)
    markets = Market.objects.filter(rangi=rangi)
    content = {"category":rangi, 'markets':markets}
    return render(request, "category.html", content)



def categories(request):  
    categories = Category.objects.all() 
    content = {"categories":categories} 
    return render(request, "categories.html", content)


class MarketDetail(DetailView):
    model = Market
    template_name = 'market_detail.html'

class Profile(TemplateView):
    template_name = 'profile.html'

def aboruds(request):
    aboruds = Aborud.objects.order_by('-title')
    return render(request, 'aboruds.html', {'aboruds':aboruds})

def mahsulot(request):
    mahsulot = Mahsulotlar.objects.order_by('-title')
    return render(request, 'mahsulotlar.html', {'mahsulotlar':mahsulot})

def seryo(request):
    seryo = Seryo.objects.order_by('-title')
    return render(request, 'seryo.html', {'seryolar':seryo})

class Delete(DeleteView):
    model = Market
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

class Edit(UpdateView):
    model = Market
    template_name = 'edit.html'
    fields=('title', 'body', 'holati', 'country', 'photo', 'rangi')

def nimadirda(request, id):
    market = Market.objects.get(id=id)
    market.saved = True
    market.save()
    return redirect('saved')
def minus(request, id):
    market = Market.objects.get(id=id)
    market.sklad = False
    market.save()
    return redirect('sklad')

def minussaved(request, id):
    market = Market.objects.get(id=id)
    market.saved = False
    market.save()
    return redirect('saved')

def kimdirda(request, id):
    market = Market.objects.get(id=id)
    market.sklad = True
    market.save()
    return redirect('sklad')



