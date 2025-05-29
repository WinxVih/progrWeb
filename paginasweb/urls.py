from django.urls import path
from .views import IndexView, SobreView
################## IMPORT CREATE
from .views import UsuarioCreate, CameraCreate, SistemaSegurancaCreate,  ProcessadorIACreate, DispositivoAutomacaoCreate, NotificacaoCreate
################# IMPORT UPDATE
from .views import UsuarioUpdate, CameraUpdate, DispositivoAutomacaoUpdate, ProcessadorIAUpdate, SistemaSegurancaUpdate, NotificacaoUpdate
################## IMPORT DELETE
from .views import UsuarioDelete, CameraDelete, SistemaSegurancaDelete, ProcessadorIADelete, DispositivoAutomacaoDelete, NotificacaoDelete
from .views import UsuarioList

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # URL para a página inicial
    path('sobre/', SobreView.as_view(), name='sobre'),  # URL para a página "Sobre"
    path('adicionar/usuario/', UsuarioCreate.as_view(), name='inserir-usuario'),
    path('adicionar/camera/', CameraCreate.as_view(), name='inserir-camera'),
    path('adicionar/sistema-seguranca/', SistemaSegurancaCreate.as_view(), name='inserir-sistema-seguranca'),
    path('adicionar/processador-ia/', ProcessadorIACreate.as_view(), name='inserir-processador-ia'),
    path('adicionar/dispositivo-automacao/', DispositivoAutomacaoCreate.as_view(), name='inserir-dispositivo-automacao'),
    path('adicionar/notificacao/', NotificacaoCreate.as_view(), name='inserir-notificacao'),
    #######
    path('atualizar/usuario/<int:pk>/', UsuarioUpdate.as_view(), name='Atualizar-usuario'),
    path('atualizar/camera/<int:pk>/', CameraUpdate.as_view(), name='Atualizar-Camera'),
    path('atualizar/sistemaSegurança/<int:pk>/', ProcessadorIAUpdate.as_view(), name='Atualizar-SistemaSegurança'),
    path('atualizar/processador-ia/<int:pk>/', SistemaSegurancaUpdate.as_view(), name='Atualizar-Processador-ia'),
    path('atualizar/dispositivo-automacao/<int:pk>/', DispositivoAutomacaoUpdate.as_view(), name='Atualizar-Dispositivo-automacao'),
    path('atualizar/notificacao/<int:pk>/', NotificacaoUpdate.as_view(), name='Atualizar-notificacao'),   
    #######
    path('deletar/usuario/<int:pk>/', UsuarioDelete.as_view(), name='Deletar-Usuario'),
    path('deletar/camera/<int:pk>/', CameraDelete.as_view(), name='Deletar-Camera'),
    path('deletar/sistemaSegurança/<int:pk>/', ProcessadorIADelete.as_view(), name='Deletar-SistemaSegurança'),
    path('deletar/processador-ia/<int:pk>/', SistemaSegurancaDelete.as_view(), name='Deletar-Processador-ia'),
    path('deletar/dispositivo-automacao/<int:pk>/', DispositivoAutomacaoDelete.as_view(), name='Deletar-Dispositivo-automacao'),
    path('deletar/notificacao/<int:pk>/', NotificacaoDelete.as_view(), name='Deletar-notificacao'),   
]
