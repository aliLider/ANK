from django.urls import path
from .views import *
from . import views
from .views import register_view, dashboard_view
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import custom_logout
from blog.views import home as h
from en.views import home as e
urlpatterns = [
    path("uz/", h, name="uz_home"),
    path('', views.home, name='ru_home'),
    path("en/", e, name="en_home"),
    path("category/<int:id>/", views.category, name="ru_category"),
    path('categories/', views.categories, name='ru_categories'),
    path('<int:pk>/', MarketDetail.as_view(), name='ru_market_detail'),
    path('<int:pk>/delete/', Delete.as_view(), name='ru_delete'),
    path('aboruds', views.aboruds, name='ru_aboruds'),
    path('mahsulot/', views.mahsulot, name='ru_mahsulot'),
    path('seryo/', views.seryo, name='ru_seryo'),
    path('<int:pk>/edit/', Edit.as_view(), name='ru_edit'),
    path('minus/<int:id>/', views.minus, name='ru_minus'),
    path('minussaved/<int:id>/', views.minussaved, name='ru_minussaved'),
    path('saved', views.saved, name='ru_saved'),
    path('sklad_1/', views.sklad_1, name='ru_sklad_1'),
    path('nimadir/<int:id>/', views.nimadirda, name='ru_nimadirda'),
    path('kimdir/<int:id>/', views.kimdirda, name='ru_kimdirda'),
    path('search/', views.search, name='ru_search'),
    path('kimdirda_1/<int:id>/', views.kimdirda_1, name='ru_kimdirda_1'),
    path('sklad/', views.sklad, name='ru_sklad'),
    path('mahsulot_savatga/<int:id>/', views.mahsulot_savatga_qoshish, name='ru_mahsulot_savatga'),
    path('aborud_savatga/<int:id>/', views.aboruds_savatga_qoshish, name='ru_aboruds_savatga'),
    path('mahsulot_savatdan_ochir/<int:id>/', views.mahsulot_savatdan_ochir, name='ru_mahsulot_savatdan_ochir'),
    path('market_savatdan_ochir/<int:id>/', views.market_savatdan_ochir, name='ru_market_savatdan_ochir'),
    path('seryo_savatdan_ochir/<int:id>/', views.seryo_savatdan_ochir, name='ru_seryo_savatdan_ochir'),
    path('aborud_savatdan_ochir/<int:id>/', views.aborud_savatdan_ochir, name='ru_aborud_savatdan_ochir'),
    path('advertisements/', views.advertisements_page, name='ru_advertisements'),
    path('register/', register_view, name='ru_register'),
    path('dashboard/', dashboard_view, name='ru_dashboard'),
    path('logout/', CustomLogoutView.as_view(next_page='/'), name='ru_logout'),
    path('blog/logout/', custom_logout, name='ru_logout'),
    path('blog/login/', LoginView.as_view(template_name='login.html'), name='ru_login'),
    path('buyurtma-berish/', views.buyurtma_berish, name='ru_buyurtma_berish'),
    path('buyurtmalar_royxati', views.buyurtmalar_royxati, name="ru_buyurtmalar_royxati")
]
