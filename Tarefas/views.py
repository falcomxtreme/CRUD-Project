from typing import Any
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse


from .models import Tarefa

class ListaDeTarefasView(ListView):
    model = Tarefa
    nome_do_template = 'tarefa_list.html'
    context_object_name = 'tarefas'

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get('status')

        if status:
            queryset = queryset.filter(status=status)
            print(status)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adiciona a lista de status ao contexto para exibição no template
        context['opcoes_status'] = Tarefa.OPCOES_STATUS
        context['status_atual'] = self.request.GET.get('status', '')
        return context

class CriarTarefa(CreateView):
    model = Tarefa
    fields = ['titulo', 'descricao', 'data_de_vencimento', 'status']
    success_url = reverse_lazy('Inicio')

class EditarTarefa(UpdateView):
    model = Tarefa
    fields = ['titulo', 'descricao', 'data_de_vencimento', 'status']
    success_url = reverse_lazy('Inicio')
    
class DeletarTarefa(DeleteView):
    model = Tarefa
    success_url = reverse_lazy('Inicio')

class ConcluirTarefa(View):
    def get(self, request, pk):
        tarefa = get_object_or_404(Tarefa, pk=pk)
        tarefa.marcar_como_completa()
        return redirect('Inicio')
