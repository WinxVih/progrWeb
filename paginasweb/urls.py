from django.urls import path
from .views import IndexView, SobreView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # URL para a página inicial
    path('sobre/', SobreView.as_view(), name='sobre'),  # URL para a página "Sobre"
    path('adicionar/usuario/', UsuarioCreate.as_view(), name='inserir-usuario'),
    path('adicionar/camera/', CameraCreate.as_view(), name='inserir-camera'),
    path('adicionar/sistema-seguranca/', SistemaSegurancaCreate.as_view(), name='inserir-sistema-seguranca'),
    path('adicionar/processador-ia/', ProcessadorIACreate.as_view(), name='inserir-processador-ia'),
    path('adicionar/dispositivo-automacao/', DispositivoAutomacaoCreate.as_view(), name='inserir-dispositivo-automacao'),
    path('adicionar/notificacao/', NotificacaoCreate.as_view(), name='inserir-notificacao'),
]
