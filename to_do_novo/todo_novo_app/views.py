from .models import Tarefa, Grupos, Sub_Grupos
from .forms import Sub_GruposForm, TarefasForm, GruposForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

#Bloco Autenticação
class Logar(LoginView):
    template_name = 'login/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('grupos')

class Registrar(FormView):
    template_name = 'login/registrar.html'
    fields = '__all__'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tarefas')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Registrar, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tarefas')
        return super(Registrar, self).get(*args, **kwargs)

class Sair(LogoutView):

    def get_success_url(self):
        return reverse_lazy('login')


#Bloco Tratamento Grupos
class VisualizaGrupo(LoginRequiredMixin, ListView, View):

    def get(self, request):
        grupos = Grupos.objects.all()
        context = {'grupos': grupos}

        return render(request, "login/grupos.html", context)

class CriarGrupo(LoginRequiredMixin, CreateView):
    model = Grupos
    context_object_name = 'criar_grupo'
    success_url = reverse_lazy('grupos')
    fields = '__all__'
    template_name = 'login/formulario_grupos.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CriarGrupo, self).form_valid(form)

class AtualizarGrupo(LoginRequiredMixin, UpdateView):
    model = Grupos
    fields = '__all__'
    success_url = reverse_lazy('grupos')
    template_name = 'login/formulario_grupos.html'

class ApagarGrupo(LoginRequiredMixin, DeleteView):
    model = Grupos
    fields = '__all__'
    success_url = reverse_lazy('grupos')
    template_name = 'login/apagar_grupo.html'



#Bloco Tratamento Sub_Grupo
class VisualizaSubGrupo(LoginRequiredMixin, ListView):

    def get(self, request, pk):
        grupo_especifico = Grupos.objects.get(id=pk)
        join_subgrupo = grupo_especifico.join_grupos.all()
        context = {'join_subgrupo': join_subgrupo, 'pk': pk}

        return render(request, "login/subgrupos.html", context)

class MostraSubGrupo(LoginRequiredMixin, View):

    def get(self, request, pk):
        subgrupo_especifico = Sub_Grupos.objects.get(id=pk)
        join_subgrupo = subgrupo_especifico.tarefa_subgrupos.all()
        context = {'join_subgrupo': join_subgrupo, 'pk': pk}

        return render(request, "login/mostra_subgrupo.html", context)


def pega_get(request, pk):

    form = Sub_GruposForm(request.POST or None)
    print(pk)
    item = Grupos.objects.get(id=pk)
    print(item)
    id_grupo = item.id
    print(id_grupo)


    if form.is_valid():
        form.save()
        return redirect(f'/subgrupos/{id_grupo}')

    return render(request, 'login/formulario_subgrupos.html', {'form': form, 'pk': pk, 'id_grupo': id_grupo})



def exclui_subgrupo(request, pk):

    item = Sub_Grupos.objects.get(id=pk)
    id_grupo = item.grupo_sub_id

    if request.method == 'POST':
        item.delete()
        return redirect(f'/subgrupos/{id_grupo}')

    return render(request, 'login/apagar_subgrupo.html', {'pk': pk, 'id_grupo': id_grupo})

def pega_get_tarefa(request, pk):

    form = TarefasForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(f'/mostra_subgrupo/{pk}')

    return render(request, 'login/formulario.html', {'form': form, 'pk': pk})


def edita_subgrupo(request, pk):

    item_id = Sub_Grupos.objects.get(id=pk)
    id_grupo = item_id.grupo_sub_id

    if request.method == 'POST':
        item = get_object_or_404(Sub_Grupos, id=pk)

        form = Sub_GruposForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(f'/subgrupos/{id_grupo}')
    else:
        item = Sub_Grupos.objects.filter(id=pk).values().last()
        form = Sub_GruposForm(initial=item)

    return render(request, 'login/formulario_subgrupos.html', {'pk': pk, 'form': form, 'id_grupo': id_grupo})



def atualiza_subgrupo(request, pk):

    item = Sub_Grupos.objects.get(id=pk)
    id_grupo = item.grupo_sub_id

    if request.method == 'POST':
        item.delete()
        return redirect(f'/subgrupos/{id_grupo}')

    return render(request, 'login/apagar_subgrupo.html', {'pk': pk, 'id_grupo': id_grupo})


class AtualizarSubGrupo(LoginRequiredMixin, UpdateView):
    model = Sub_Grupos
    fields = '__all__'
    template_name = 'login/formulario_subgrupos.html'



#Bloco Tratamento Tarefas
class ListaTarefa(LoginRequiredMixin, ListView):
    model = Tarefa
    fields = '__all__'
    context_object_name = 'tarefas'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['tarefas'] = data['tarefas'].filter(user=self.request.user)
        data['count'] = data['tarefas'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            data['tarefas'] = data['tarefas'].filter(
                title__startswith=search_input)
        data['search_input'] = search_input
        return data

class TodasTarefas(LoginRequiredMixin, ListView):
    model = Tarefa
    context_object_name = 'completo'

class Criar(LoginRequiredMixin, CreateView):
    model = Tarefa
    fields = '__all__'
    success_url = reverse_lazy('tarefas')
    template_name = 'login/formulario.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Criar, self).form_valid(form)

class Atualizar(LoginRequiredMixin, UpdateView):
    model = Tarefa
    fields = '__all__'
    success_url = reverse_lazy('tarefas')
    template_name = 'login/formulario.html'

class Apagar(DeleteView, LoginRequiredMixin):
    model = Tarefa
    fields = '__all__'
    success_url = reverse_lazy('tarefas')
    template_name = 'login/confirmar.html'

def exclui_tarefa(request, pk):

    item_tarefa = Tarefa.objects.get(id=pk)
    id_subgrupo = item_tarefa.subgrupo_tar_id

    if request.method == 'POST':
        item.delete()
        return redirect(f'/tarefas/{id_subgrupo}')

    return render(request, 'login/confirmar.html', {'pk': pk, 'id_subgrupo': id_subgrupo})

def edita_tarefa(request, pk):

    item_tarefa = Tarefa.objects.get(id=pk)
    id_subgrupo = item_tarefa.subgrupo_tar_id

    if request.method == 'POST':
        item = get_object_or_404(Sub_Grupos, id=pk)

        form = TarefasForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(f'/tarefas/{id_subgrupo}')
    else:
        item = Tarefa.objects.filter(id=pk).values().last()
        form = TarefasForm(initial=item)

    return render(request, 'login/tarefa_list.html', {'pk': pk, 'form': form, 'id_subgrupo': id_subgrupo})
