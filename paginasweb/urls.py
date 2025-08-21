from django.urls import path
from .views import IndexView, SobreView
################## IMPORT CREATE
from .views import CameraCreate, SistemaSegurancaCreate,  ProcessadorIACreate, DispositivoAutomacaoCreate, NotificacaoCreate
################# IMPORT UPDATE
from .views import  CameraUpdate, DispositivoAutomacaoUpdate, ProcessadorIAUpdate, SistemaSegurancaUpdate, NotificacaoUpdate
################## IMPORT DELETE
from .views import  CameraDelete, SistemaSegurancaDelete, ProcessadorIADelete, DispositivoAutomacaoDelete, NotificacaoDelete
##################IMPORT LIS
from .views import CameraList, SistemaSegurancaList, ProcessadorList, DispositivoAutomacaoList, NotificacaoList
from django.contrib.auth import views as auth_views
from .views import CadastroUsuarioView


urlpatterns = [
    #Criar rota para página de login
    path("registrar/", CadastroUsuarioView.as_view(), name="registrar"),
    path("login/", auth_views.LoginView.as_view(
        template_name = 'paginasweb/form.html',
        extra_context = {
        'titulo' : 'Autenticar',
        'botao' : 'Entrar',
    }
    ), name="login"),

    #Criar uma rota de logout
    path("sair/", auth_views.LogoutView.as_view(
        template_name = 'paginasweb/form.html',
        extra_context = {
        'titulo' : 'Deslogar',
        'botao' : 'Sair',
    }
    ), name="logout"),
    
    #Criar uma rota de senha
    path("atualizar/", auth_views.PasswordChangeView.as_view(
        template_name = 'paginasweb/form.html',
        extra_context = {
        'titulo' : 'Atualizar_Senha',
        'botao' : 'Atualizar',
    }
    ), name="senha"),

    path('', IndexView.as_view(), name='index'),  # URL para a página inicial
    path('sobre/', SobreView.as_view(), name='sobre'),  # URL para a página "Sobre"
    path('adicionar/camera/', CameraCreate.as_view(), name='inserir-camera'),
    path('adicionar/sistema-seguranca/', SistemaSegurancaCreate.as_view(), name='inserir-sistema-seguranca'),
    path('adicionar/processador-ia/', ProcessadorIACreate.as_view(), name='inserir-processador-ia'),
    path('adicionar/dispositivo-automacao/', DispositivoAutomacaoCreate.as_view(), name='inserir-dispositivo-automacao'),
    path('adicionar/notificacao/', NotificacaoCreate.as_view(), name='inserir-notificacao'),
    #######
    path('atualizar/camera/<int:pk>/', CameraUpdate.as_view(), name='Atualizar-Camera'),
    path('atualizar/sistemaSegurança/<int:pk>/', ProcessadorIAUpdate.as_view(), name='Atualizar-SistemaSegurança'),
    path('atualizar/processador-ia/<int:pk>/', SistemaSegurancaUpdate.as_view(), name='Atualizar-Processador-ia'),
    path('atualizar/dispositivo-automacao/<int:pk>/', DispositivoAutomacaoUpdate.as_view(), name='Atualizar-Dispositivo-automacao'),
    path('atualizar/notificacao/<int:pk>/', NotificacaoUpdate.as_view(), name='Atualizar-notificacao'),   
    #######
    path('deletar/camera/<int:pk>/', CameraDelete.as_view(), name='Deletar-Camera'),
    path('deletar/sistemaSegurança/<int:pk>/', ProcessadorIADelete.as_view(), name='Deletar-SistemaSegurança'),
    path('deletar/processador-ia/<int:pk>/', SistemaSegurancaDelete.as_view(), name='Deletar-Processador-ia'),
    path('deletar/dispositivo-automacao/<int:pk>/', DispositivoAutomacaoDelete.as_view(), name='Deletar-Dispositivo-automacao'),
    path('deletar/notificacao/<int:pk>/', NotificacaoDelete.as_view(), name='Deletar-notificacao'),   
    #########################
    path('listar/camera/', CameraList.as_view(), name='Listar-Camera'),
    path('listar/processador/', ProcessadorList.as_view(), name='Listar-Processador'),
    path('listar/sistemaSeguranca/', SistemaSegurancaList.as_view(), name='Listar-SistemaSeguranca'),
    path('listar/dispositivoAutomacao/', DispositivoAutomacaoList.as_view(), name='Listar-DispositioAutomacao'),
    path('listar/notificacao/', NotificacaoList.as_view(), name='Listar-Notificacao'),
]
