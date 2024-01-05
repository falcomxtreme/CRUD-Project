from typing import Any
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect


from .models import Tarefa
from .filters import FiltroDeTarefas


def inicio(request):
    filto_de_tarefa = FiltroDeTarefas(request.GET, queryset=Tarefa.objects.all())
    context = {
        'form': filto_de_tarefa.form,
        'tarfa': filto_de_tarefa.qs
    }
    return render(request, 'tarefa_list.html', context)


class ListaDeTarefasView(ListView):
    queryset= Tarefa.objects.all()
    nome_do_template = 'tarefa_list.html'
    context_object_name = 'tarefas'
    
    def get_queryset(self):
        querySet = super().get_queryset()
        self.filterset = FiltroDeTarefas(self.request.GET, queryset=querySet)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context
    
class CriarTarefa(CreateView):
    model = Tarefa
    fields = ["Titulo", "Descricao", "DataDeVencimento", "Status"]
    success_url = reverse_lazy("inicio")

class EditarTarefa(UpdateView):
    model = Tarefa
    fields = ["Titulo", "Descricao", "DataDeVencimento", "Status"]
    success_url = reverse_lazy("inicio")
    
class DeletarTarefa(DeleteView):
    model = Tarefa
    success_url = reverse_lazy("inicio")

class ConcluirTarefa(View):
    
    def get(self, request, pk):
        tarefa = get_object_or_404(Tarefa, pk=pk)
        tarefa.MarcarComoCompleta()
        return redirect("inicio")