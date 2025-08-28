from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView,UpdateView, DeleteView 
from .models import Camera,Sistema_Seguranca,Processador_IA,Dispositivo_Automacao,Notificacao
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from .forms import UsuarioCadastroForm
from django.shortcuts import get_object_or_404


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

    # pega o usuário autenticado e atribui ao campo usuario
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class SistemaSegurancaCreate(LoginRequiredMixin, CreateView):
    model = Sistema_Seguranca
    template_name = 'paginasweb/form.html'
    fields = ['nome']  
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Cadastrar sistema de seguranca',
        'botao' : 'Cadastrar',
    }
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class ProcessadorIACreate(LoginRequiredMixin, CreateView):
    model = Processador_IA
    template_name = 'paginasweb/form.html'
    fields = ['modelo', 'confiabilidade']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Cadastrar processador',
        'botao' : 'Cadastrar',
    }
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class DispositivoAutomacaoCreate(LoginRequiredMixin, CreateView):
    model = Dispositivo_Automacao
    template_name = 'paginasweb/form.html'
    fields = ['tipo', 'estado']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Cadastrar dispositivo de automacao',
        'botao' : 'Cadastrar',
    }
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class NotificacaoCreate(LoginRequiredMixin, CreateView):
    model = Notificacao
    template_name = 'paginasweb/form.html'
    fields = ['tipo']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Cadastrar notificacao',
        'botao' : 'Cadastrar',
    }
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

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

    def get_object(self, queryset=None):
        obj = get_object_or_404(Camera, pk=self.kwargs.get('pk'), usuario=self.request.user)
        return obj

class ProcessadorIAUpdate(UpdateView):
    model = Processador_IA
    template_name = 'paginasweb/form.html'
    fields = ['modelo', 'confiabilidade']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Atualização de dados do Processador',
        'botao' : 'Salvar',
    }

    def get_object(self, queryset=None):
        obj = get_object_or_404(Processador_IA, pk=self.kwargs.get('pk'), usuario=self.request.user)
        return obj

class DispositivoAutomacaoUpdate(UpdateView):
    model = Dispositivo_Automacao
    template_name = 'paginasweb/form.html'
    fields = ['tipo', 'estado']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Atualização de dados do Dispositivo de Automacao',
        'botao' : 'Salvar',
    }

    def get_object(self, queryset=None):
        obj = get_object_or_404(Dispositivo_Automacao, pk=self.kwargs.get('pk'), usuario=self.request.user)
        return obj

class SistemaSegurancaUpdate(UpdateView):
    model = Sistema_Seguranca
    template_name = 'paginasweb/form.html'
    fields = ['nome']  
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Atualização de dados do Sistema de Segurança',
        'botao' : 'Salvar',
    }

    def get_object(self, queryset=None):
        obj = get_object_or_404(Sistema_Seguranca, pk=self.kwargs.get('pk'), usuario=self.request.user)
        return obj

class NotificacaoUpdate(UpdateView):
    model = Notificacao
    template_name = 'paginasweb/form.html'
    fields = ['tipo']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Atualização de dados da Notificação',
        'botao' : 'Salvar',
    }

    def get_object(self, queryset=None):
        obj = get_object_or_404(Notificacao, pk=self.kwargs.get('pk'), usuario=self.request.user)
        return obj

######################################### DELETE


class CameraDelete(DeleteView):
    model = Camera
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Deletar Camera',
        'botao' : 'Excluir',
    }

    def get_object(self, queryset=None):
        obj = get_object_or_404(Camera, pk=self.kwargs.get('pk'), usuario=self.request.user)
        return obj


class ProcessadorIADelete(DeleteView):
    model = Processador_IA
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Deletar Processador',
        'botao' : 'Excluir',
    }

    def get_object(self, queryset=None):
        obj = get_object_or_404(Processador_IA, pk=self.kwargs.get('pk'), usuario=self.request.user)
        return obj
    

class DispositivoAutomacaoDelete(DeleteView):
    model = Dispositivo_Automacao
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Deletar Disoositivo de Automacao',
        'botao' : 'Excluir',
    }

    def get_object(self, queryset=None):
        obj = get_object_or_404(Dispositivo_Automacao, pk=self.kwargs.get('pk'), usuario=self.request.user)
        return obj
    

class NotificacaoDelete(DeleteView):
    model = Notificacao
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Deletar Notificacao',
        'botao' : 'Excluir',
    }
    def get_object(self, queryset=None):
        obj = get_object_or_404(Notificacao, pk=self.kwargs.get('pk'), usuario=self.request.user)
        return obj


class SistemaSegurancaDelete(DeleteView):
    model = Sistema_Seguranca
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo' : 'Deletar Sistema de Seguranca',
        'botao' : 'Excluir',
    }
    def get_object(self, queryset=None):
        obj = get_object_or_404(Sistema_Seguranca, pk=self.kwargs.get('pk'), usuario=self.request.user)
        return obj


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


# Views que listam só os registros do usuário logado

class UsuarioCameraList(ListView):
    model = Camera
    template_name = 'paginasweb/list/cameraList.html'

    def get_queryset(self):
        # Filtra as câmeras pelo usuário logado
        return Camera.objects.filter(usuario=self.request.user)


class UsuarioProcessadorList(ListView):
    model = Processador_IA
    template_name = 'paginasweb/list/processadorList.html'

    def get_queryset(self):
        # Filtra os processadores pelo usuário logado
        return Processador_IA.objects.filter(usuario=self.request.user)


class UsuarioDispositivoAutomacaoList(ListView):
    model = Dispositivo_Automacao
    template_name = 'paginasweb/list/dispositivoAutomacaoList.html'

    def get_queryset(self):
        # Filtra os dispositivos pelo usuário logado
        return Dispositivo_Automacao.objects.filter(usuario=self.request.user)


class UsuarioNotificacaoList(ListView):
    model = Notificacao
    template_name = 'paginasweb/list/notificacaoList.html'

    def get_queryset(self):
        # Filtra as notificações pelo usuário logado
        return Notificacao.objects.filter(usuario=self.request.user)


class UsuarioSistemaSegurancaList(ListView):
    model = Sistema_Seguranca
    template_name = 'paginasweb/list/sistemaSegurancaList.html'

    def get_queryset(self):
        # Filtra os sistemas de segurança pelo usuário logado
        return Sistema_Seguranca.objects.filter(usuario=self.request.user)
