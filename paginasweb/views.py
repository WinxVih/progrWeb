from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView,UpdateView, DeleteView 
from .models import Camera,Sistema_Seguranca,Processador_IA,Dispositivo_Automacao,Notificacao
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from .forms import UsuarioCadastroForm


# Crie a view no final do arquivo ou em outro local que faça sentido
class CadastroUsuarioView(CreateView):
    model = User
    # Não tem o fields, pois ele é definido no forms.py
    form_class = UsuarioCadastroForm
    # Pode utilizar o seu form padrão
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('login')
    extra_context = {'titulo': 'Registro de usuários'}


    def form_valid(self, form):
        # Faz o comportamento padrão do form_valid
        url = super().form_valid(form)
        # Busca ou cria um grupo com esse nome
        grupo, criado = Group.objects.get_or_create(name='Estudante')
        # Acessa o objeto criado e adiciona o usuário no grupo acima
        self.object.groups.add(grupo)
        # Retorna a URL de sucesso
        return url


# Criação das listas

class IndexView(TemplateView):
    template_name = 'paginasweb/index.html'  

class SobreView(TemplateView):
    template_name = 'paginasweb/sobre.html'

class CameraCreate(LoginRequiredMixin, CreateView):
    model = Camera
    template_name = 'paginasweb/form.html'
    fields = ['ip', 'status']  
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Cadastrar camera',
        'botao' : 'Cadastrar',
    }


class SistemaSegurancaCreate(LoginRequiredMixin, CreateView):
    model = Sistema_Seguranca
    template_name = 'paginasweb/form.html'
    fields = ['nome']  
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Cadastrar sistema de seguranca',
        'botao' : 'Cadastrar',
    }


class ProcessadorIACreate(LoginRequiredMixin, CreateView):
    model = Processador_IA
    template_name = 'paginasweb/form.html'
    fields = ['modelo', 'confiabilidade']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Cadastrar processador',
        'botao' : 'Cadastrar',
    }


class DispositivoAutomacaoCreate(LoginRequiredMixin, CreateView):
    model = Dispositivo_Automacao
    template_name = 'paginasweb/form.html'
    fields = ['tipo', 'estado']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Cadastrar dispositivo de automacao',
        'botao' : 'Cadastrar',
    }


class NotificacaoCreate(LoginRequiredMixin, CreateView):
    model = Notificacao
    template_name = 'paginasweb/form.html'
    fields = ['tipo']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Cadastrar notificacao',
        'botao' : 'Cadastrar',
    }

################################## UPDATE


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

#####################################LISTAS


class CameraList(ListView):
    model = Camera
    template_name = 'paginasweb/list/cameraList.html'


class ProcessadorList(ListView):
    model = Processador_IA
    template_name = 'paginasweb/list/processadorList.html'


class DispositivoAutomacaoList(ListView):
    model = Dispositivo_Automacao
    template_name = 'paginasweb/list/dispositivoAutomacaoList.html'


class NotificacaoList(ListView):
    model = Notificacao
    template_name = 'paginasweb/list/notificacaoList.html'


class SistemaSegurancaList(ListView):
    model = Sistema_Seguranca
    template_name = 'paginasweb/list/sistemaSegurancaList.html'
