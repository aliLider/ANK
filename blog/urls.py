from django.urls import path
from .views import *
from . import views
from .views import register_view, dashboard_view
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import custom_logout
from ru.views import home as h
from en.views import home as e


urlpatterns = [
    # path('', Home.as_view(), name = 'home'),
    path('', views.home, name='uz_home'),
    path("ru/", h, name="ru_home"),
    path("en/", e, name="en_home"),
    path("category/<int:id>/", views.category, name="category"),
    path('categories/', views.categories, name='categories'),
    path('<int:pk>/', MarketDetail.as_view(), name='market_detail'),
    path('<int:pk>/delete/', Delete.as_view(), name='delete'),
    path('aboruds', views.aboruds, name='aboruds'),
    path('mahsulot/', views.mahsulot, name='mahsulot'),
    path('seryo/', views.seryo, name='seryo'),
    path('<int:pk>/edit/', Edit.as_view(), name='edit'),
    path('minus/<int:id>/',views.minus, name='minus'),
    path('minussaved/<int:id>/',views.minussaved, name='minussaved'),
    path('saved', views.saved, name='saved'),  #dfghjkllllkjcjkasdbajdnasnakjsns,amaskx
    path('sklad_1/', views.sklad_1, name='sklad_1'),
    path('nimadir/<int:id>/', views.nimadirda, name='nimadirda'),
    path('kimdir/<int:id>/',views.kimdirda, name='kimdirda'),
    path('search/', views.search, name='search'),
    path('kimdirda_1/<int:id>/', views.kimdirda_1, name='kimdirda_1'),
    path('sklad/', views.sklad, name='sklad'),
    path('mahsulot_savatga/<int:id>/', views.mahsulot_savatga_qoshish, name='mahsulot_savatga'),
    path('aborud_savatga/<int:id>/', views.aboruds_savatga_qoshish, name='aboruds_savatga'),
    path('mahsulot_savatdan_ochir/<int:id>/', views.mahsulot_savatdan_ochir, name='mahsulot_savatdan_ochir'),
    path('market_savatdan_ochir/<int:id>/', views.market_savatdan_ochir, name='market_savatdan_ochir'),
    path('seryo_savatdan_ochir/<int:id>/', views.seryo_savatdan_ochir, name='seryo_savatdan_ochir'),
    path('aborud_savatdan_ochir/<int:id>/', views.aborud_savatdan_ochir, name='aborud_savatdan_ochir'),
    path('advertisements/', views.advertisements_page, name='advertisements'),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', CustomLogoutView.as_view(next_page='/'), name='logout'),
    path('blog/logout/', custom_logout, name='logout'),
    path('blog/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('buyurtma-berish/', views.buyurtma_berish, name='buyurtma_berish'),
    path('buyurtmalar_royxati', views.buyurtmalar_royxati, name="buyurtmalar_royxati")
]
