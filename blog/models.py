from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    titles = models.CharField(max_length=200, verbose_name='Rangi', null=True)

    def __str__(self):
        return self.titles



class Market(models.Model):
    UZ = 'uz'
    RU = 'ru'
    EN = 'en'
    CHOISE_GROUP_lang = {
        (UZ , 'uz'),
        (RU , 'ru'),
        (EN , 'en')
    }
    group_lang = models.CharField(max_length=100 , choices=CHOISE_GROUP_lang , default=UZ)
    title = models.CharField(max_length=200, null=True, verbose_name='Mahsulot nomi')
    body = models.CharField(max_length=200, null=True, verbose_name='Asl narxi')
    holati = models.CharField(max_length=200, null=True, verbose_name='holati')
    country = models.CharField(max_length=200, blank=True, null=True, verbose_name='Davlati')
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    saved = models.BooleanField('Saqlangan', default=False)
    sklad = models.BooleanField('korzina', default=False)
    created_at = models.DateTimeField(default=now, verbose_name='Qo‘shilgan vaqt')  # Yangi maydon

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('market_detail', args=[str(self.id)])
    def get_absolute_url(self):
        return reverse('home2_detail', args=[str(self.id)])


class Aborud(models.Model):
    UZ = 'uz'
    RU = 'ru'
    EN = 'en'
    CHOISE_GROUP_lang = {
        (UZ , 'uz'),
        (RU , 'ru'),
        (EN , 'en')
    }
    group_lang = models.CharField(max_length=100 , choices=CHOISE_GROUP_lang , default=UZ)
    title = models.CharField(max_length=200, verbose_name='Mashinani nomi', null=True)
    photo = models.ImageField(upload_to='images/', blank=True)
    holati = models.CharField(max_length=200, null=True)
    body = models.CharField(max_length=200, null=True, verbose_name='Narxi')
    sklad = models.BooleanField(default=False, verbose_name='Savatga qo\'shilganmi')
    created_at = models.DateTimeField(default=now, verbose_name='Qo‘shilgan vaqt')

    def __str__(self):
        return self.title

class Mahsulotlar(models.Model):
    UZ = 'uz'
    RU = 'ru'
    EN = 'en'
    CHOISE_GROUP_lang = {
        (UZ , 'uz'),
        (RU , 'ru'),
        (EN , 'en')
    }
    group_lang = models.CharField(max_length=100 , choices=CHOISE_GROUP_lang , default=UZ)
    title = models.CharField(max_length=200, verbose_name='Mahsulot nomi', null=True)
    qalinligi = models.CharField(max_length=200, verbose_name='Mahsulotni qalinligi', null=True)
    razmeri = models.CharField(max_length=200, verbose_name='Mahsulotni razmeri', null=True)
    photo = models.ImageField(upload_to='images/', blank=True)
    body = models.CharField(max_length=200, null=True, verbose_name='Narxi')
    sklad = models.BooleanField(default=False, verbose_name='Savatga qo\'shilganmi')
    created_at = models.DateTimeField(default=now, verbose_name='Qo‘shilgan vaqt')  # Yangi maydon

    def __str__(self):
        return self.title


class Seryo(models.Model):
    UZ = 'uz'
    RU = 'ru'
    EN = 'en'
    CHOISE_GROUP_lang = {
        (UZ , 'uz'),
        (RU , 'ru'),
        (EN , 'en')
    }
    group_lang = models.CharField(max_length=100 , choices=CHOISE_GROUP_lang , default=UZ)
    title = models.CharField(max_length=200, verbose_name='Mahsulot nomi', null=True)
    photo = models.ImageField(upload_to='images/', blank=True)
    markasi = models.CharField(max_length=200, verbose_name='Markasi', null=True)
    body = models.CharField(max_length=200, null=True, verbose_name='Narxi')
    sklad_1 = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now, verbose_name='Qo‘shilgan vaqt')


    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('seryo_detail', args=[str(self.id)])



class Advertisement(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)  # Bo'sh qiymatlar uchun ruxsat
    image = models.ImageField(upload_to='advertisements', blank=True, null=True)
class CustomUser(AbstractUser):
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

# models.py
class Buyurtma(models.Model):
    foydalanuvchi = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    mahsulot_nomi = models.TextField(verbose_name="Mahsulotlar ro'yxati")
    umumiy_summa = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Umumiy summa")
    umumiy_kg = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Umumiy kilogramm")
    buyurtma_vaqti = models.DateTimeField(auto_now_add=True, verbose_name="Buyurtma vaqti")
    foydalanuvchi_kiritgan_kg = models.JSONField(default=dict, verbose_name="Foydalanuvchi kilogrammi")  # JSONField
    tasdiqlandi = models.BooleanField(default=False, verbose_name="Tasdiqlanganmi")  # Yangi maydon

    def __str__(self):
        return f"Buyurtma #{self.id} - {self.foydalanuvchi.username} - {self.buyurtma_vaqti} - {self.foydalanuvchi.phone_number} - {self.foydalanuvchi.address}"
