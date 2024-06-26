from django.urls import path
from apps.usuarios.views import login, cadastro, logout 

urlpatterns = [
    path('login', login, name='login'),#login->é o caminho da url
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),
]