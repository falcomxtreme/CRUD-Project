import django_filters
from .models import Tarefa


class FiltroDeTarefas(django_filters.FilterSet):

    class Meta:
        model = Tarefa
        fields = {
            'Status': ['exact'],
        }