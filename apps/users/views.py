from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from apps.users.forms import SignInForms, SignUpForms

def sign_in(request):
    form = SignInForms()
    if request.method == 'POST':
        form = SignInForms(request.POST)

        if form.is_valid():
            name=form["name"].value()
            password=form["password"].value()
        
        user = auth.authenticate(
            request,
            username=name,
            password=password
        )
        if user is not None:
            auth.login(request, user)
            messages.success(request, f"Usuário {name} logado com sucesso")
            return redirect('index')
        else:
            messages.error(request, "Usuário e/ou senha inválidos")
            return redirect('sign_in')

    return render(request, 'users/sign_in.html',{'form': form})

def sign_up(request):

    form = SignUpForms()
    if request.method == 'POST':
        form = SignUpForms(request.POST)
        if form.is_valid():

            name=form["name"].value()
            email=form["email"].value()
            password=form["password_create"].value()

            if User.objects.filter(username=name).exists():
                messages.error(request, "usuário ja existente")
                return redirect('sign_up')
            
            user = User.objects.create_user(
                username=name,
                email=email,
                password=password
            )
            user.save()
            messages.success(request, "Cadastro efetuado com sucesso")
            return redirect('sign_in')

    return render(request, 'users/sign_up.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout realizado com sucesso")
    return redirect('sign_in')