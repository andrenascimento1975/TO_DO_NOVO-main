from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Grupos(models.Model):
    nome_grupo = models.CharField(max_length=100, null=False, blank=True)

    def __str__(self):
        return self.nome_grupo

class Sub_Grupos(models.Model):
    nome_subgrupo = models.CharField(max_length=100, null=False, blank=True)
    grupo_sub = models.ForeignKey(Grupos, on_delete=models.CASCADE, null=True, blank=True, related_name='join_grupos')

    def __str__(self):
        return self.nome_subgrupo

    def get_absolute_url(self):
        return reverse('grupos')

        #return reverse('grupos', kwargs={'pk': self.pk})

class Tarefa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE, null=True, blank=True, related_name='tarefa_grupos')
    sub_grupo = models.ForeignKey(Sub_Grupos, on_delete=models.CASCADE, null=True, blank=True, related_name='tarefa_subgrupos')
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('subgrupos', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['complete']