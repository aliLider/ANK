from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Foydalanuvchilar

class FoydalanuvchilarCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Foydalanuvchilar
        fields=UserCreationForm.Meta.fields+('age', 'address', 'email')


class FoydalanuvchilarChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        models=Foydalanuvchilar
        fields = UserChangeForm.Meta.fields
