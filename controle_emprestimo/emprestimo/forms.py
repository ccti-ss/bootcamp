from django import forms
from .models import Usuario, Objeto, Emprestimo
#usuário
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  

    class Meta:

        model = User
        fields = ['username', 'email', 'password1','password2']
        
class UsuarioForm (forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome','matricula', 'curso','email']

class ObjetoForm (forms.ModelForm):
    class Meta:
        model = Objeto
        fields = ['nome', 'descricao','quantidade_disponivel']

class EmprestimoForm (forms.ModelForm): 
    class Meta:
        model = Emprestimo
        fields = ['usuario', 'objeto', 'data_devolucao', 'status']

