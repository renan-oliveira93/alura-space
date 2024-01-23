from django import forms

class SignInForms(forms.Form):
    name=forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
                widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: João Silva"
            }
        )
    )
    password=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )

class SignUpForms(forms.Form):
    name=forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
                widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: João Silva"
            }
        )
    )
    email=forms.CharField(
        label="Email",
        required=True,
        max_length=100,
                widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite seu email: xpto@gmail.com"
            }
        )
    )
    password_create=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
    password_confirmation=forms.CharField(
        label="Confirme sua senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha mais uma vez"
            }
        )
    )