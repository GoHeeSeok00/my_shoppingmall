from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='비밀번호 확인', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "password", "name", "email", "gender", "date_of_birth", "mobile_number", "introduce",
                  "is_seller", "is_terms_of_service", "is_privacy_policy", "is_receive_marketing_info")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ("username", "password", "name", "email", "gender", "date_of_birth", "mobile_number", "introduce",
                  "is_seller", "is_terms_of_service", "is_privacy_policy", "is_receive_marketing_info")

    def clean_password(self):
        return self.initial["password"]