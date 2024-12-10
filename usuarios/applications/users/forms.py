from django import forms

from .models import user

class UserRegisterForm(forms.ModelForm):
    
    password1=forms.CharField(
        label="contrasena",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"Contrasena"
            }
        )
    )
    password2=forms.CharField(
        label="contrasena",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"Repetir Contrasena"
            }
        )
    )

    class Meta:
        model = user 
        fields = (
            "username",
            "email",
            "nombres",
            "apellidos",
            "genero",
            "is_staff"
        )
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contrasenas no son las mismas")
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    

class LoginForm(forms.Form):
    username=forms.CharField(
        label="usuario",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Usuario"
            }
        )
    )
    password=forms.CharField(
        label="contrasena",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"Contrasena"
            }
        )
    )