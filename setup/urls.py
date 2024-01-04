from django.contrib import admin
from django.urls import path

from Tarefas.views import ListaDeTarefas, CriarTarefa, EditarTarefa, DeletarTarefa, ConcluirTarefa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListaDeTarefas.as_view(), name="ListaDeTarefas"),
    path("criar", CriarTarefa.as_view(), name="CriarTarefa"),
    path("editar/<int:pk>", EditarTarefa.as_view(), name="EditarTarefa"),
    path("excluir/<int:pk>", DeletarTarefa.as_view(), name="DeletarTarefa"),
    path("concluir/<int:pk>", ConcluirTarefa.as_view(), name="ConcluirTarefa"),
]
