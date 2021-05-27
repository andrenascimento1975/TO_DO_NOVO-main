from django.contrib import admin
from .models import Tarefa, Grupos, Sub_Grupos

admin.site.register(Grupos)
admin.site.register(Sub_Grupos)
admin.site.register(Tarefa)