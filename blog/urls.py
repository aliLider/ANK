from django.urls import path
from .views import *
from . import views
urlpatterns = [
    # path('', Home.as_view(), name = 'home'),
    path('', views.home, name='home'),
    path("category/<int:id>/", views.category, name="category"),
    path('categories/', views.categories, name='categories'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile', Profile.as_view(), name='profile'),
    path('<int:pk>/', MarketDetail.as_view(), name='market_detail'),
    path('<int:pk>/delete/', Delete.as_view(), name='delete'),
    path('aboruds', views.aboruds, name='aboruds'),
    path('mahsulot/', views.mahsulot, name='mahsulot'),
    path('seryo/', views.seryo, name='seryo'),
    path('<int:pk>/edit/', Edit.as_view(), name='edit'),
    path('minus/<int:id>/',views.minus, name='minus'),
    path('minussaved/<int:id>/',views.minussaved, name='minussaved'),
    path('saved', views.saved, name='saved'),  #dfghjkllllkjcjkasdbajdnasnakjsns,amaskx
    path('sklad/', views.sklad, name='sklad'),
    path('nimadir/<int:id>/', views.nimadirda, name='nimadirda'),
    path('kimdir/<int:id>/',views.kimdirda, name='kimdirda'),
    path('search/', views.search, name='search'),


]