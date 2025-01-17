from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
class CustomUserCreationForm(UserCreationForm):
    address = forms.CharField(
        max_length=255, 
        required=True, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Manzilingizni kiriting',
            'class': 'form-control',
        }),
        help_text="Manzilni ko'rsating (masalan: Toshkent, Yunusobod tumani, 5-uy)"
    )
    phone_number = forms.CharField(
        max_length=15, 
        required=True, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Shaxsiy raqam +998987654321',
            'class': 'form-control',
        }),
        help_text="Telefon raqamni kiritishda xalqaro formatdan foydalaning (masalan: +998901234567)"
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'address', 'phone_number' , 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Foydalanuvchi nomi kiriting',
                'class': 'form-control',
                'id': 'id_username'
            }),
            'password1': forms.PasswordInput(attrs={
                'placeholder': 'Parolni kiriting',
                'class': 'form-control',
            }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': 'Parolni tasdiqlang',
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Elektron pochtangizni kiriting',
                'class': 'form-control',
            }),
        }
        help_texts = {
            'username': "Foydalanuvchi nomi 150 ta belgidan oshmasligi kerak. Harflar, raqamlar va @/./+/-/_ belgilari ruxsat etilgan.",
            'password1': "Parol kamida 8 ta belgidan iborat bo'lishi va maxsus belgilarni o'z ichiga olishi kerak.",
            'password2': "Yuqorida kiritilgan parolni tasdiqlang.",
        }       
