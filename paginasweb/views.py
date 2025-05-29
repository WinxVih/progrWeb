from django.views.generic import TemplateView
from django.views.generic.edit import CreateView,UpdateView, DeleteView 
from .models import Usuario,Camera,Sistema_Seguranca,Processador_IA,Dispositivo_Automacao,Notificacao
from django.urls import reverse_lazy

# Criação das listas



class IndexView(TemplateView):
    template_name = 'paginasweb/index.html'  

class SobreView(TemplateView):
    template_name = 'paginasweb/sobre.html'

class UsuarioCreate(CreateView):
    model = Usuario
    template_name = 'paginasweb/form.html'
    fields = ['nome']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Cadastrar Usuario',
        'botao' : 'Cadastrar',
    }

class CameraCreate(CreateView):
    model = Camera
    template_name = 'paginasweb/form.html'
    fields = ['ip', 'status']  
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Cadastrar camera',
        'botao' : 'Cadastrar',
    }

class SistemaSegurancaCreate(CreateView):
    model = Sistema_Seguranca
    template_name = 'paginasweb/form.html'
    fields = ['nome']  
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Cadastrar sistema de seguranca',
        'botao' : 'Cadastrar',
    }

class ProcessadorIACreate(CreateView):
    model = Processador_IA
    template_name = 'paginasweb/form.html'
    fields = ['modelo', 'confiabilidade']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Cadastrar processador',
        'botao' : 'Cadastrar',
    }

class DispositivoAutomacaoCreate(CreateView):
    model = Dispositivo_Automacao
    template_name = 'paginasweb/form.html'
    fields = ['tipo', 'estado']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Cadastrar dispositivo de automacao',
        'botao' : 'Cadastrar',
    }

class NotificacaoCreate(CreateView):
    model = Notificacao
    template_name = 'paginasweb/form.html'
    fields = ['tipo']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Cadastrar notificacao',
        'botao' : 'Cadastrar',
    }

################################## UPDATE
class UsuarioUpdate(UpdateView):
    model = Usuario
    template_name = 'paginasweb/form.html'
    fields = ['nome']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Atualização de dados do Usuario',
        'botao' : 'Salvar',
    }

class CameraUpdate(UpdateView):
    model = Camera
    template_name = 'paginasweb/form.html'
    fields = ['ip', 'status']  
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Atualização de dados da Camera',
        'botao' : 'Salvar',
    }

class ProcessadorIAUpdate(UpdateView):
    model = Processador_IA
    template_name = 'paginasweb/form.html'
    fields = ['modelo', 'confiabilidade']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Atualização de dados do Processador',
        'botao' : 'Salvar',
    }

class DispositivoAutomacaoUpdate(UpdateView):
    model = Dispositivo_Automacao
    template_name = 'paginasweb/form.html'
    fields = ['tipo', 'estado']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Atualização de dados do Dispositivo de Automacao',
        'botao' : 'Salvar',
    }

class SistemaSegurancaUpdate(UpdateView):
    model = Sistema_Seguranca
    template_name = 'paginasweb/form.html'
    fields = ['nome']  
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Atualização de dados do Sistema de Segurança',
        'botao' : 'Salvar',
    }

class NotificacaoUpdate(UpdateView):
    model = Notificacao
    template_name = 'paginasweb/form.html'
    fields = ['tipo']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Atualização de dados da Notificação',
        'botao' : 'Salvar',
    }

######################################### DELETE

class UsuarioDelete(DeleteView):
    model = Usuario
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Deletar Usuario',
        'botao' : 'Excluir',
    }

class CameraDelete(DeleteView):
    model = Camera
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Deletar Camera',
        'botao' : 'Excluir',
    }

class ProcessadorIADelete(DeleteView):
    model = Processador_IA
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Deletar Processador',
        'botao' : 'Excluir',
    }

class DispositivoAutomacaoDelete(DeleteView):
    model = Dispositivo_Automacao
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Deletar Disoositivo de Automacao',
        'botao' : 'Excluir',
    }

class NotificacaoDelete(DeleteView):
    model = Notificacao
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Deletar Notificacao',
        'botao' : 'Excluir',
    }

class SistemaSegurancaDelete(DeleteView):
    model = Sistema_Seguranca
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Deletar Sistema de Seguranca',
        'botao' : 'Excluir',
    }

class UsuarioList(ListView):
    model = Usuario
    template_name = 'paginasweb/usuario.html'
    

    