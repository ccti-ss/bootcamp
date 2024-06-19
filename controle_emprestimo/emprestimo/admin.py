from django.contrib import admin

from .models import Usuario, Objeto, Emprestimo

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome','matricula', 'curso', 'email')


@admin.register(Objeto)
class ObjetoAdmin(admin.ModelAdmin):
    list_display = ('nome','descricao', 'quantidade_disponivel')

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    
    list_display = ('usuario', 'objeto', 'data_emprestimo', 'data_devolucao', 'status')

    list_filter = ('status', 'data_emprestimo')
    
    search_fields = ('usuario__nome', 'objeto__nome')
