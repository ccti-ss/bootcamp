from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adicionar/',views.adicionar_emprestimo, name='adicionar_emprestimo'),
    path('lista/', views.lsita_emprestimo, name='lista_emprestimo'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/login/',views.login_view, name='login_accounts'),

]

