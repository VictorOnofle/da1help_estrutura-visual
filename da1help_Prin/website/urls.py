from django.urls import path
from . import views

urlpatterns = [
    # path('caminho_no_navegador/', funcao_da_view, name='nome_interno_da_rota')
    
    path('', views.pagina_inicial, name='home'),
    path('contato/', views.contato, name='contato'),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('esqueci-senha/', views.esqueci_senha, name='esqueci_senha'),
    path('busca/', views.busca, name='busca'),
    path('sobre/', views.sobre, name='sobre'),
]