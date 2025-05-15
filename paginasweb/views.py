from django.views.generic import TemplateView
from django.views.generic.edit import CreateView,UpdateView, DeleteView 
from .models import Usuario,Camera,Sistema_Seguranca,Processador_IA,Dispositivo_Automacao,Notificacao
from django.urls import reverse_lazy

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

class SistemaSegurancaCreate(CreateView):
    model = Sistema_Seguranca
    template_name = 'paginasweb/form.html'
    fields = ['nome']  
    success_url = reverse_lazy('index')

class ProcessadorIACreate(CreateView):
    model = Processador_IA
    template_name = 'paginasweb/form.html'
    fields = ['modelo', 'confiabilidade']
    success_url = reverse_lazy('index')

class DispositivoAutomacaoCreate(CreateView):
    model = Dispositivo_Automacao
    template_name = 'paginasweb/form.html'
    fields = ['tipo', 'estado']
    success_url = reverse_lazy('index')

class NotificacaoCreate(CreateView):
    model = Notificacao
    template_name = 'paginasweb/form.html'
    fields = ['tipo']
    success_url = reverse_lazy('index')

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

class ProcessadorIAUpdate(UpdateView):
    model = Processador_IA
    template_name = 'paginasweb/form.html'
    fields = ['modelo', 'confiabilidade']
    success_url = reverse_lazy('index')

class DispositivoAutomacaoUpdate(UpdateView):
    model = Dispositivo_Automacao
    template_name = 'paginasweb/form.html'
    fields = ['tipo', 'estado']
    success_url = reverse_lazy('index')

class SistemaSegurancaUpdate(UpdateView):
    model = Sistema_Seguranca
    template_name = 'paginasweb/form.html'
    fields = ['nome']  
    success_url = reverse_lazy('index')

class NotificacaoUpdate(UpdateView):
    model = Notificacao
    template_name = 'paginasweb/form.html'
    fields = ['tipo']
    success_url = reverse_lazy('index')

######################################### DELETE

class UsuarioDelete(DeleteView):
    model = Usuario
    template_name = 'paginasweb/form.html'
    fields = ['nome']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Atualização de dados do Usuario',
        'botao' : 'Salvar',
    }

class CameraDelete(DeleteView):
    model = Camera
    template_name = 'paginasweb/form.html'
    fields = ['ip', 'status']  
    success_url = reverse_lazy('index')

class ProcessadorIADelete(DeleteView):
    model = Processador_IA
    template_name = 'paginasweb/form.html'
    fields = ['modelo', 'confiabilidade']
    success_url = reverse_lazy('index')

class DispositivoAutomacaoDelete(DeleteView):
    model = Dispositivo_Automacao
    template_name = 'paginasweb/form.html'
    fields = ['tipo', 'estado']
    success_url = reverse_lazy('index')

class NotificacaoDelete(DeleteView):
    model = Notificacao
    template_name = 'paginasweb/form.html'
    fields = ['tipo']
    success_url = reverse_lazy('index')

class SistemaSegurancaDelete(DeleteView):
    model = Sistema_Seguranca
    template_name = 'paginasweb/form.html'
    fields = ['tipo', 'estado']
    success_url = reverse_lazy('index')