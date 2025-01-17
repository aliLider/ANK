from django.shortcuts import render
# Create your views here.
from django.shortcuts import render,redirect
from django.views.generic import DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from blog.models import *
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
# from .models import Advertisement
from blog.forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from decimal import Decimal, InvalidOperation
from blog.admin import BuyurtmaAdmin
def zakazlar_royxati(request):
    tasdiqlangan_zakazlar = Zakaz.objects.filter(tasdiqlandi=True)
    return render(request, 'ru/zakazlar.html', {'zakazlar': tasdiqlangan_zakazlar})

def advertisements_page(request):
    advertisements = Advertisement.objects.all()
    return render(request, 'ru/advertisements.html', {'advertisements': advertisements})

def search(request):
    query = request.GET.get('search')
    results = []
    resultsa = []
    resultss = []
    resultsm = []

    if query:
        # Qidiruvni bir nechta maydonlarda amalga oshirish
        results = Market.objects.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query) |
            Q(country__icontains=query) |
            # Q(rangi__icontains=query) |
            Q(holati__icontains=query)
        )
        resultss = Seryo.objects.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query) |
            # Q(country__icontains=query) |
            Q(markasi__icontains=query) 
            # Q(holati__icontains=query)
        )
        resultsa = Aborud.objects.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query) |
            Q(holati__icontains=query) 
            # Q(markasi__icontains=query) 
            # Q(holati__icontains=query)
        )
        resultsm = Mahsulotlar.objects.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query) 
            # Q(holati__icontains=query) 
            # Q(markasi__icontains=query) 
            # Q(holati__icontains=query)
        )
    return render(request, 'ru/search.html', {'query': query, 'search_obj': results , 'search_objs': resultss , 'search_objsa': resultsa , 'search_objsm': resultsm})
def saved(request):
    # saqlash = Market.objects.all()
    saved = Market.objects.filter(saved=True)
    return render(request, 'ru/saved.html', {'saved':saved})

def sklad(request):
    sklad = Market.objects.filter(sklad=True)
    return render(request, 'ru/sklad.html', {'sklad':sklad})
def sklad_1(request):
    sklad_1 = Seryo.objects.filter(sklad_1=True)
    return render(request, 'ru/sklad.html', {'sklad_1':sklad_1})
def home(request):
    markets = Market.objects.order_by('-title')
    advertisements = Advertisement.objects.all()
    return render (request, 'ru/home.html', {'markets':markets , "advertisements":advertisements})

def category(request, id):
    rangi = Category.objects.get(id=id)
    markets = Market.objects.filter(rangi=rangi)
    content = {"category":rangi, 'markets':markets}
    return render(request, "ru/category.html", content)



def categories(request):
    categories = Category.objects.all()
    content = {"categories":categories}
    return render(request, "ru/categories.html", content)


class MarketDetail(DetailView):
    model = Market
    template_name = 'market_detail.html'


def aboruds(request):
    aboruds = Aborud.objects.order_by('-title')
    return render(request, 'ru/aboruds.html', {'aboruds':aboruds})

def mahsulot(request):
    mahsulot = Mahsulotlar.objects.order_by('-title')
    return render(request, 'ru/mahsulotlar.html', {'mahsulotlar':mahsulot})

def seryo(request):
    seryo = Seryo.objects.order_by('-title')
    return render(request, 'ru/seryo.html', {'seryolar':seryo})

class Delete(DeleteView):
    model = Market
    template_name = 'ru/delete.html'
    success_url = reverse_lazy('home')

class Edit(UpdateView):
    model = Market
    template_name = 'ru/edit.html'
    fields=('title', 'body', 'holati', 'country', 'photo', 'rangi')

def nimadirda(request, id):
    market = Market.objects.get(id=id)
    market.saved = True
    market.save()
    return redirect('ru_saved')
def minus(request, id):
    market = Market.objects.get(id=id)
    market.sklad = False
    market.save()
    return redirect('ru_sklad')

def minussaved(request, id):
    market = Market.objects.get(id=id)
    market.saved = False
    market.save()
    return redirect('ru_saved')

def kimdirda(request, id):
    market = Market.objects.get(id=id)
    market.sklad = True
    market.save()
    return redirect('ru_sklad')

def kimdirda_1(request, id):
    seryo = Seryo.objects.get(id=id)
    seryo.sklad_1= True
    seryo.save()
    return redirect('ru_sklad_1')

def sklad(request):
    sklad = Market.objects.filter(sklad=True)
    return render(request, 'ru_sklad.html', {'sklad': sklad})
def sklad(request):
    market_sklad = Market.objects.filter(sklad=True)
    seryo_sklad = Seryo.objects.filter(sklad_1=True)
    return render(request, 'ru_sklad.html', {
        'market_sklad': market_sklad,
        'seryo_sklad': seryo_sklad,
    })
def kimdirda(request, id):
    try:
        market = Market.objects.get(id=id)
        market.sklad = True
        market.save()
        return redirect('ru_sklad')
    except Market.DoesNotExist:
        return redirect('ru_home')  # Xatolik yuz berganda asosiy sahifaga qaytadi
def aboruds_savatga_qoshish(request, id):
    try:
        aborud = Aborud.objects.get(id=id)
        aborud.sklad = True
        aborud.save()
        return redirect('ru_sklad')  # Yoki kerakli sahifaga qaytish
    except Aborud.DoesNotExist:
        return redirect('ru_home')  # Agar topilmasa, asosiy sahifaga qaytish
def aboruds(request):
    aboruds = Aborud.objects.order_by('-title')
    print(aboruds)
    return render(request, 'ru/aboruds.html', {'aboruds': aboruds})

def kimdirda_1(request, id):
    try:
        seryo = Seryo.objects.get(id=id)
        seryo.sklad_1 = True
        quantity = request.POST.get('quantity', 10)  # Default: 10 kg
        total_price = int(quantity) * seryo.body  # Narxni hisoblash
        print(f"Kiritilgan kilogramm: {quantity}, Jami summa: {total_price}")  # Test uchun
        seryo.save()
        return redirect('ru_sklad')
    except Seryo.DoesNotExist:
        return redirect('ru_home')

def mahsulot_savatga_qoshish(request, id):
    try:
        mahsulot = Mahsulotlar.objects.get(id=id)
        mahsulot.sklad = True
        quantity = request.POST.get('quantity', 10)  # Default qiymat: 10
        print(f"Kiritilgan kilogramm: {quantity}")  # Test uchun konsolga chiqaramiz
        mahsulot.save()
        return redirect('ru_sklad')  # Savat sahifasiga qaytish
    except Mahsulotlar.DoesNotExist:
        return redirect('ru_home')  # Topilmasa asosiy sahifaga qaytish


def kimdirda(request, id):
    print(f"Mahsulot ID: {id}")
    market = Market.objects.get(id=id)
    market.sklad = True
    market.created_at = now()  # Qo‘shilgan vaqtni yangilash
    market.save()
    return redirect('ru_sklad')

def sklad(request):
    market_sklad = Market.objects.filter(sklad=True).order_by('-created_at')
    seryo_sklad = Seryo.objects.filter(sklad_1=True).order_by('-created_at')
    aborud_sklad = Aborud.objects.filter(sklad=True).order_by('-created_at')
    mahsulot_sklad = Mahsulotlar.objects.filter(sklad=True).order_by('-created_at')

    return render(request, 'ru/sklad.html', {
        'market_sklad': market_sklad,
        'seryo_sklad': seryo_sklad,
        'aborud_sklad': aborud_sklad,
        'mahsulot_sklad': mahsulot_sklad,
    })


def mahsulot_savatdan_ochir(request, id):
    try:
        mahsulot = Mahsulotlar.objects.get(id=id)
        mahsulot.sklad = False
        mahsulot.save()
        return redirect('ru_sklad')  # Savat sahifasiga qaytish
    except Mahsulotlar.DoesNotExist:
        return redirect('ru_sklad')  # Agar mahsulot topilmasa, savatga qaytish

def market_savatdan_ochir(request, id):
    try:
        market = Market.objects.get(id=id)
        market.sklad = False
        market.save()
        return redirect('ru_sklad')  # Savat sahifasiga qaytish
    except Market.DoesNotExist:
        return redirect('ru_sklad')
def seryo_savatdan_ochir(request, id):
    try:
        seryo = Seryo.objects.get(id=id)
        seryo.sklad_1 = False
        seryo.save()
        return redirect('ru_sklad')  # Savat sahifasiga qaytish
    except Seryo.DoesNotExist:
        return redirect('ru_sklad')
def aborud_savatdan_ochir(request, id):
    try:
        aborud = Aborud.objects.get(id=id)
        aborud.sklad = False
        aborud.save()
        return redirect('ru_sklad')  # Savat sahifasiga qaytish
    except Aborud.DoesNotExist:
        return redirect('ru_sklad')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('ru_home')  # Redirect to dashboard on success
    else:
        form = CustomUserCreationForm()
    return render(request, 'ru/register.html', {'form': form})

# 4. Login View


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')  # 'username' is used here because AuthenticationForm uses 'username' by default
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', 'dashboard')  # Default to 'dashboard' if 'next' is not provided
                return redirect(next_url)
            else:
                return render(request, 'ru/login.html', {'form': form, 'error': 'Invalid credentials'})
        else:
            return render(request, 'ru/login.html', {'form': form, 'error': 'Invalid form submission'})
    else:
        form = AuthenticationForm()
        return render(request, 'ru/login.html', {'form': form})

@login_required
def dashboard_view(request):
    user = request.user
    tasdiqlangan_buyurtmalar = Buyurtma.objects.filter(tasdiqlandi=True).order_by("-buyurtma_vaqti")[:1]
    tasdiqlanmagan_buyurtmalar = Buyurtma.objects.filter(tasdiqlandi=False).order_by("-buyurtma_vaqti")[:5]
    return render(request, 'ru/dashboard.html', {
        'username': user.username,
        'email': user.email,
        'address': user.address,
        'phone_number': user.phone_number,
        'tasdiqlangan_buyurtmalar': tasdiqlangan_buyurtmalar,
        'tasdiqlanmagan_buyurtmalar': tasdiqlanmagan_buyurtmalar
    })
def logout_view(request):
    logout(request)  # Foydalanuvchini tizimdan chiqaradi
    return redirect('')
class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "Siz tizimdan muvaffaqiyatli chiqdingiz.")
        return super().dispatch(request, *args, **kwargs)

def custom_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('ru_home'))


def to_decimal(value):
    """Convert the value to Decimal format."""
    """Qiymatni Decimal formatiga o'tkazish"""
    try:
        # Check for invalid or empty values
        # Yaroqsiz yoki bo'sh qiymatlarni tekshirish
        if value in [None, '', 'Narxi mavjud emas']:
            return Decimal('0.00')

        return Decimal(value)
    except (InvalidOperation, TypeError, ValueError):
        # Return 0.00 if the value cannot be converted to Decimal
        return Decimal('0.00')
@login_required
def buyurtma_berish(request):
    if request.method == 'POST':
        # Faqat skladdagi mahsulotlarni yig'ish
        market_sklad = Market.objects.filter(sklad=True)
        seryo_sklad = Seryo.objects.filter(sklad_1=True)
        aborud_sklad = Aborud.objects.filter(sklad=True)
        mahsulot_sklad = Mahsulotlar.objects.filter(sklad=True)
        foydalanuvchi_kiritgan_kg = {}
        umumiy_summa = 0
        umumiy_kg = 0
        if not (market_sklad.exists() or seryo_sklad.exists() or aborud_sklad.exists() or mahsulot_sklad.exists()):
            messages.error(request, "Avval mahsulot tanlang!")
            return redirect('ru_sklad')  # Sklad sahifasiga qaytarish
        # Buyurtma ma'lumotlarini yaratish
        buyurtma_malumotlari = "Buyurtma berilgan mahsulotlar:\n\n"
        # Market mahsulotlari
        for market in market_sklad:
            price_per_kg = float(market.body) # Mahsulotning narxi
            total = price_per_kg
            buyurtma_malumotlari += f"{market.title} - {price_per_kg} so'm = Jami: {total} so'm\n"
            umumiy_summa += total

        for seryo in seryo_sklad:
            kg = float(request.POST.get(f"kg_{seryo.id}", 10))
            price_per_kg = float(seryo.body)  # Mahsulotning narxi
            total = kg * price_per_kg
            buyurtma_malumotlari += f"{seryo.title} - {price_per_kg} so'm * {kg} kg = Jami: {total} so'm\n"
            umumiy_summa += total
            umumiy_kg += kg

        for aborud in aborud_sklad:
            price_per_kg = float(aborud.body)
            total = price_per_kg
            buyurtma_malumotlari += f"{aborud.title} - {price_per_kg} so'm = Jami: {total} so'm\n"
            umumiy_summa += total

        for mahsulot in mahsulot_sklad:
            kg = float(request.POST.get(f"kg_{mahsulot.id}", 10))  # Kilogrammni inputdan olish
            price_per_kg = float(mahsulot.body)  # Mahsulotning narxi
            total = kg * price_per_kg
            buyurtma_malumotlari += f"{mahsulot.title} - {price_per_kg} so'm * {kg} kg = Jami: {total} so'm\n"
            umumiy_summa += total
            umumiy_kg += kg


        # Buyurtmani saqlash
        Buyurtma.objects.create(
            foydalanuvchi=request.user,
            mahsulot_nomi=buyurtma_malumotlari,
            umumiy_summa=umumiy_summa,
            umumiy_kg=umumiy_kg,  # Umumiy kilogrammni saqlash
            foydalanuvchi_kiritgan_kg=foydalanuvchi_kiritgan_kg,
        )

        # Mahsulotlarni savatdan olib tashlash
        market_sklad.update(sklad=False)
        seryo_sklad.update(sklad_1=False)
        aborud_sklad.update(sklad=False)
        mahsulot_sklad.update(sklad=False)

        messages.success(request, f"Buyurtma muvaffaqiyatli yuborildi! ({umumiy_kg} kg) - Jami summa: {umumiy_summa} so'm")
        return redirect('ru_sklad')

    return redirect('ru_sklad')

def buyurtmalar_royxati(request):
    tasdiqlangan_buyurtmalar = Buyurtma.objects.filter(tasdiqlandi=True).order_by("-buyurtma_vaqti")
    tasdiqlanmagan_buyurtmalar = Buyurtma.objects.filter(tasdiqlandi=False).order_by("-buyurtma_vaqti")
    return render(
        request,
        'ru/buyurtmalar.html',
        {
            'tasdiqlangan_buyurtmalar': tasdiqlangan_buyurtmalar,
            'tasdiqlanmagan_buyurtmalar': tasdiqlanmagan_buyurtmalar,
        }
    )
