from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Foydalanuvchilar(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name='Age')
    address = models.CharField(max_length=200, verbose_name='Location')
    email = models.EmailField(max_length=200)


class Category(models.Model):
    titles = models.CharField(max_length=200, verbose_name='Rangi')

    def __str__(self):
        return self.titles
    


class Market(models.Model):
    title = models.CharField(max_length=200, null=True, verbose_name='Mahsulot nomi')
    body = models.CharField(max_length=200, null=True, verbose_name='Asl narxi')
    holati = models.CharField(max_length=200, null=True, verbose_name='holati')
    country = models.CharField(max_length=200, blank=True, null=True, verbose_name='Davlati')
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    rangi = models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name='Rangi', null=True)
    tell = models.CharField(max_length=200, blank=True, null=True, verbose_name='Telefon')
    telegram = models.CharField(max_length=200, blank=True, null=True, verbose_name='telegram')
    saved = models.BooleanField('Saqlangan', default=False)
    sklad = models.BooleanField('korzina', default=False)
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('market_detail', args=[str(self.id)])
    def get_absolute_url(self):
        return reverse('home2_detail', args=[str(self.id)])
   

class Aborud(models.Model):
    title = models.CharField(max_length=200, verbose_name='Mashinani nomi', null=True)
    photo = models.ImageField(upload_to='images/', blank=True)
    holati = models.CharField(max_length=200, null=True)
    body = models.CharField(max_length=200, null=True, verbose_name='Narxi')
   
    def __str__(self):
        return self.title

class Mahsulotlar(models.Model):
    title = models.CharField(max_length=200, verbose_name='Mahsulot nomi', null=True)
    qalinligi = models.CharField(max_length=200, verbose_name='Mahsulotni qalinligi', null=True)
    razmeri = models.CharField(max_length=200, verbose_name='Mahsulotni razmeri', null=True)
    photo = models.ImageField(upload_to='images/', blank=True)
    rangi = models.ForeignKey(Market, on_delete = models.CASCADE, verbose_name='Markasi', null=True)
    body = models.CharField(max_length=200, null=True, verbose_name='Narxi')    

    def __str__(self):
        return self.title
    

class Seryo(models.Model):
    title = models.CharField(max_length=200, verbose_name='Mahsulot nomi', null=True)
    photo = models.ImageField(upload_to='images/', blank=True)
    markasi = models.ForeignKey(Market, on_delete = models.CASCADE, verbose_name='Markasi', null=True)
    body = models.CharField(max_length=200, null=True, verbose_name='Narxi')    

    def __str__(self):
        return self.title            