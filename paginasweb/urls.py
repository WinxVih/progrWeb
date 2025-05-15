from django.urls import path
from .views import IndexView, SobreView
################## IMPORT CREATE
from .views import UsuarioCreate, CameraCreate, SistemaSegurancaCreate,  ProcessadorIACreate, DispositivoAutomacaoCreate, NotificacaoCreate
################# IMPORT UPDATE
from .views import UsuarioUpdate, CameraUpdate, DispositivoAutomacaoUpdate, ProcessadorIAUpdate, SistemaSegurancaUpdate, NotificacaoUpdate
################## IMPORT DELETE
from .views import UsuarioDelete, CameraDelete, SistemaSegurancaDelete, ProcessadorIADelete, DispositivoAutomacaoDelete, NotificacaoDelete
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
    path('atualizar/Usuario/', UsuarioUpdate.as_view(), name='Atualizar-usuario'),
    path('atualizar/Camera/', CameraUpdate.as_view(), name='Atualizar-Camera'),
    path('atualizar/SistemaSegurança/', ProcessadorIAUpdate.as_view(), name='Atualizar-SistemaSegurança'),
    path('atualizar/Processador-ia/', SistemaSegurancaUpdate.as_view(), name='Atualizar-Processador-ia'),
    path('atualizar/Dispositivo-automacao/', DispositivoAutomacaoUpdate.as_view(), name='Atualizar-Dispositivo-automacao'),
    path('atualizar/notificacao/', NotificacaoUpdate.as_view(), name='Atualizar-notificacao'),   
    #######
    path('Deletar/Usuario/', UsuarioDelete.as_view(), name='Deletar-Usuario'),
    path('Deletar/Camera/', CameraDelete.as_view(), name='Deletar-Camera'),
    path('Deletar/SistemaSegurança/', ProcessadorIADelete.as_view(), name='Deletar-SistemaSegurança'),
    path('Deletar/Processador-ia/', SistemaSegurancaDelete.as_view(), name='Deletar-Processador-ia'),
    path('Deletar/Dispositivo-automacao/', DispositivoAutomacaoDelete.as_view(), name='Deletar-Dispositivo-automacao'),
    path('Deletar/notificacao/', NotificacaoDelete.as_view(), name='Deletar-notificacao'),   
]
