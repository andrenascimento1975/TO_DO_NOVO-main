from django.urls import path
from .models import Tarefa, Grupos, Sub_Grupos
from .views import Logar, Registrar, ListaTarefa, TodasTarefas, VisualizaGrupo, VisualizaSubGrupo, Criar, CriarGrupo, Atualizar, \
    AtualizarGrupo, AtualizarSubGrupo, Apagar, ApagarGrupo, MostraSubGrupo, pega_get, pega_get_tarefa, exclui_subgrupo, edita_subgrupo, exclui_tarefa, edita_tarefa
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView

urlpatterns = [
    path('tarefas/<int:pk>', ListaTarefa.as_view(), name='tarefas'),
    path('login/', Logar.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('registrar/', Registrar.as_view(), name='registrar'),
    path('todas/', TodasTarefas.as_view(), name='completo'),
    path('', VisualizaGrupo.as_view(), name='grupos'),
    path('subgrupos/<int:pk>', VisualizaSubGrupo.as_view(), name='subgrupos'),
    path('criar/<int:pk>', pega_get_tarefa, name='criar'),
    path('criar_grupo/', CriarGrupo.as_view(), name='criar_grupo'),
    path('criar_subgrupo/<int:pk>', pega_get, name='criar_subgrupo'),
    path('atualizar/<int:pk>', edita_tarefa, name='atualizar'),
    path('atualizar_grupos/<int:pk>', AtualizarGrupo.as_view(), name='atualizar_grupos'),
    path('atualizar_subgrupos/<int:pk>', edita_subgrupo, name='atualizar_subgrupos'),
    path('apagar/<int:pk>', exclui_tarefa, name='apagar'),
    path('apagar_grupo/<int:pk>', ApagarGrupo.as_view(), name='apagar_grupo'),
    path('apagar_subgrupo/<int:pk>', exclui_subgrupo, name='apagar_subgrupo'),
    path('mostra_subgrupo/<int:pk>', MostraSubGrupo.as_view(), name='mostra_subgrupo'),
]
