from typing import Any
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .models import Tarefa
from .filters import FiltroDeTarefas

class ListaDeTarefas(ListView):
    model = Tarefa

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = FiltroDeTarefas(self.request.GET,
          queryset=self.get_queryset()
        )
        return context

class CriarTarefa(CreateView):
    model = Tarefa
    fields = ["Titulo", "Descricao", "DataDeVencimento", "Status"]
    success_url = reverse_lazy("ListaDeTarefas")

class EditarTarefa(UpdateView):
    model = Tarefa
    fields = ["Titulo", "Descricao", "DataDeVencimento", "Status"]
    success_url = reverse_lazy("ListaDeTarefas")
    
class DeletarTarefa(DeleteView):
    model = Tarefa
    success_url = reverse_lazy("ListaDeTarefas")

class ConcluirTarefa(View):
    
    def get(self, request, pk):
        tarefa = get_object_or_404(Tarefa, pk=pk)
        tarefa.MarcarComoCompleta()
        return redirect("ListaDeTarefas")