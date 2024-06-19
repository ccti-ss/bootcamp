from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm, ObjetoForm, EmprestimoForm, UserRegisterForm
from .models import Emprestimo
from django.contrib import messages

# Create your views here.

def index (request):
    return render(request, 'emprestimo/index.html')


def register (request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)

            login(request)
            return redirect('index')
        
        else:
            
            form = UserRegisterForm()

            return render(request,'emprestimo/register.html', {'form': form})
        
def login_view(request):

   if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            print(f"{username} e {password}")
            user = authenticate(username=username, password=password)

            if user is not None:
               login(request, user)
               print('foi?')
               return redirect('index')
            else:
                print('erro user')
                messages.error(request, "Usuário ou senha incorretos.")
        else:
            messages.error(request, "Usuário ou senha incorretos.")
            print('erro valid')
   else:
        
        form = AuthenticationForm()
        
        return render(request, 'emprestimo/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')





@login_required
def adicionar_emprestimo(request):
    
    if request.method == "POST":

        form = EmprestimoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_emprestimo')
    
    else:
        form = EmprestimoForm()
        return render(request, 'emprestimo/adicionar_emprestimo.html ', {'form':form})

@login_required
def lsita_emprestimo(request):

    emprestimos = Emprestimo.objects.all()
    return render(request, 'emprestimo/lista_emprestimos.html', {"emprestimos": emprestimos})

