from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Buyurtma
from .models import CustomUser, Advertisement, Market, Category, Aborud, Mahsulotlar, Seryo
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number',)}),  # Adjust based on actual model fields
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number',)}),  # Adjust based on actual model fields
    )

def tasdiqlash(modeladmin, request, queryset):
    queryset.update(tasdiqlandi=True)
class BuyurtmaAdmin(admin.ModelAdmin):
    list_display = ('foydalanuvchi', 'umumiy_kg', 'umumiy_summa', 'buyurtma_vaqti', 'foydalanuvchi_kiritgan_kg', 'tasdiqlandi')  # Tasdiqlangan statusini qo'shish
    search_fields = ('foydalanuvchi__username', 'umumiy_summa')
    actions = [tasdiqlash]  # Tasdiqlash actionini qo'shish


admin.action(description='Tanlangan buyurtmalarni tasdiqlash')
admin.site.register(Buyurtma, BuyurtmaAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Category)
admin.site.register(Market)
admin.site.register(Aborud)
admin.site.register(Mahsulotlar)
admin.site.register(Seryo)
admin.site.register(Advertisement)
