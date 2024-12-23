from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', views.salafan, name='malumot'),
    path('seryo_srm/', views.seryo, name='seryo_srm'),
    path('aborud_srm/', views.aborud, name='aborud_srm'),
    path('plus/', Malumotqushish.as_view(), name='plus'),
    path('seryoplus/', SeryoQushish.as_view(), name='seryoplus'),
    path('aborudqushish/', AborudQushish.as_view(), name = 'aborudqushish'),
    path('sotilganmahsulotlar/', SotilganMahsulotlar.as_view(), name='sotilganmahsulotlar'),
    path('<int:pk>/', Home2detail.as_view(), name='home2_detail')
]