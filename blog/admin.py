from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import FoydalanuvchilarChangeForm, FoydalanuvchilarCreationForm
from .models import Foydalanuvchilar, Market, Category,Aborud, Mahsulotlar, Seryo
# Register your models here.

class FoydalanuvchilarUserAdmin(UserAdmin):
    add_form=FoydalanuvchilarCreationForm
    form = FoydalanuvchilarChangeForm
    model = Foydalanuvchilar
    list_display = ['email', 'address', 'age', 'username']

admin.site.register(Foydalanuvchilar, FoydalanuvchilarUserAdmin)
admin.site.register(Market)
admin.site.register(Category)
admin.site.register(Aborud)
admin.site.register(Mahsulotlar)
admin.site.register(Seryo)