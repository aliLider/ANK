from django.urls import path
from .views import *
from . import views
from .views import register_view, dashboard_view
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import custom_logout
from blog.views import home as h
from en.views import home as e
from ru.views import home as r

urlpatterns = [
    path("uz/", h, name="uz_home"),
    path('ru/', r, name='ru_home'),
    path('', e, name='en_home'),
    path("category/<int:id>/", views.category, name="en_category"),
    path('categories/', views.categories, name='en_categories'),
    path('<int:pk>/', MarketDetail.as_view(), name='en_market_detail'),
    path('<int:pk>/delete/', Delete.as_view(), name='en_delete'),
    path('aboruds/', views.aboruds, name='en_aboruds'),
    path('mahsulot/', views.mahsulot, name='en_mahsulot'),
    path('seryo/', views.seryo, name='en_seryo'),
    path('<int:pk>/edit/', Edit.as_view(), name='en_edit'),
    path('minus/<int:id>/', views.minus, name='en_minus'),
    path('minussaved/<int:id>/', views.minussaved, name='en_minussaved'),
    path('saved', views.saved, name='en_saved'),
    path('sklad_1/', views.sklad_1, name='en_sklad_1'),
    path('nimadir/<int:id>/', views.nimadirda, name='en_nimadirda'),
    path('kimdir/<int:id>/', views.kimdirda, name='en_kimdirda'),
    path('search/', views.search, name='en_search'),
    path('kimdirda_1/<int:id>/', views.kimdirda_1, name='en_kimdirda_1'),
    path('sklad/', views.sklad, name='en_sklad'),
    path('mahsulot_savatga/<int:id>/', views.mahsulot_savatga_qoshish, name='en_mahsulot_savatga'),
    path('aborud_savatga/<int:id>/', views.aboruds_savatga_qoshish, name='en_aboruds_savatga'),
    path('mahsulot_savatdan_ochir/<int:id>/', views.mahsulot_savatdan_ochir, name='en_mahsulot_savatdan_ochir'),
    path('market_savatdan_ochir/<int:id>/', views.market_savatdan_ochir, name='en_market_savatdan_ochir'),
    path('seryo_savatdan_ochir/<int:id>/', views.seryo_savatdan_ochir, name='en_seryo_savatdan_ochir'),
    path('aborud_savatdan_ochir/<int:id>/', views.aborud_savatdan_ochir, name='en_aborud_savatdan_ochir'),
    path('advertisements/', views.advertisements_page, name='en_advertisements'),
    path('register/', register_view, name='en_register'),
    path('dashboard/', dashboard_view, name='en_dashboard'),
    path('logout/', CustomLogoutView.as_view(next_page='/'), name='en_logout'),
    path('blog/logout/', custom_logout, name='en_logout'),
    path('blog/login/', LoginView.as_view(template_name='login.html'), name='en_login'),
    path('buyurtma-berish/', views.buyurtma_berish, name='en_buyurtma_berish'),
    path('buyurtmalar_royxati', views.buyurtmalar_royxati, name="en_buyurtmalar_royxati")
]
